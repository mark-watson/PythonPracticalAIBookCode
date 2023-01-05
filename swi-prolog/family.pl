parent(X, Y) :- mother(X, Y).
parent(X, Y) :- father(X, Y).
grandparent(X, Z) :-
  parent(X, Y),
  parent(Y, Z).
