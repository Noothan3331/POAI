% Facts
likes(mary, food).
likes(mary, wine).
likes(john, wine).
likes(john, mary).

% Rules
likes(john, X) :- likes(mary, X).       % John likes anything that Mary likes.
likes(john, X) :- likes(X, wine).       % John likes anyone who likes wine.
likes(john, X) :- likes(X, X).          % John likes anyone who likes themselves.

% Initialization goal
:- initialization(main).

main :-
    % Running queries and printing results
    (likes(mary, food) -> write('Mary likes food'), nl ; write('Mary does not like food'), nl),
    (likes(john, wine) -> write('John likes wine'), nl ; write('John does not like wine'), nl),
    (likes(john, food) -> write('John likes food'), nl ; write('John does not like food'), nl).
