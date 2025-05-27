# Knowledge Base: Rules in IF-THEN format
knowledge_base = [
    (["cough", "fever"], "flu"),
    (["sore_throat", "runny_nose"], "cold"),
    (["sore_throat"], "fever")  # Sore throat can lead to fever
]

# Given initial facts
facts = {"cough", "sore_throat"}

# Forward Chaining Function
def forward_chaining():
    inferred = True  # Keep looping as long as new facts are added
    while inferred:
        inferred = False  # Stop if no new fact is added in an iteration
        for conditions, conclusion in knowledge_base:
            if all(condition in facts for condition in conditions) and conclusion not in facts:
                facts.add(conclusion)  # Add the inferred fact
                inferred = True  # Mark that we inferred a new fact

# Run forward chaining
forward_chaining()

# Check if flu or cold is inferred
if "flu" in facts:
    print("The patient is diagnosed with flu.")
elif "cold" in facts:
    print("The patient is diagnosed with cold.")
else:
    print("No conclusive diagnosis could be made.")
