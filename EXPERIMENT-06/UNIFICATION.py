# Unification logic
def unify(x, y, theta={}):
    if theta is None:
        return None
    elif x == y:
        return theta
    elif isinstance(x, str) and x.islower():
        return unify_var(x, y, theta)
    elif isinstance(y, str) and y.islower():
        return unify_var(y, x, theta)
    elif isinstance(x, list) and isinstance(y, list) and len(x) == len(y):
        return unify(x[1:], y[1:], unify(x[0], y[0], theta))
    else:
        return None

def unify_var(var, x, theta):
    if var in theta:
        return unify(theta[var], x, theta)
    elif x in theta:
        return unify(var, theta[x], theta)
    else:
        theta[var] = x
        return theta

# Substitute variables based on theta
def substitute(predicate, theta):
    return [theta.get(x, x) for x in predicate]

# Resolution logic
def resolution(kb, facts, query):
    for clause in kb:
        premise, conclusion = clause
        for fact in facts:
            theta = unify(premise, fact, {})
            if theta is not None:
                inferred = substitute(conclusion, theta)
                if inferred == query:
                    return True
    return False

# Knowledge base: Human(x) → Mortal(x)
knowledge_base = [
    [["Human", "x"], ["Mortal", "x"]]
]

# Fact: Human(John)
facts = [["Human", "John"]]

# Query: Mortal(John)?
query = ["Mortal", "John"]

# Apply resolution
if resolution(knowledge_base, facts, query):
    print("Query is resolved: John is Mortal")
else:
    print("Query could not be resolved")
