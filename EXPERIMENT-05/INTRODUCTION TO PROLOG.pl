:- initialization(main).

max(X, Y, X) :- X >= Y.
max(X, Y, Y) :- X < Y.

main :-
    max(3, 5, Max),
    write(Max), nl.
