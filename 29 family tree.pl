% Facts about family relationships
father(john, lisa).
father(mike, emma).
father(tom, mary).

mother(mary, lisa).
mother(mary, mike).
mother(emma, olivia).

% Rules to infer additional relationships
parent(X, Y) :- father(X, Y).
parent(X, Y) :- mother(X, Y).

sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.

grandfather(X, Y) :- father(X, Z), parent(Z, Y).

grandmother(X, Y) :- mother(X, Z), parent(Z, Y).
