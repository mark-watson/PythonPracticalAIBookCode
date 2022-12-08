/*
  Solve the N Quenns problem. From the Swi-Prolog documentation:
     https://www.swi-prolog.org/pldoc/man?section=clpfd-n-queens
*/

n_queens(N, Qs) :-
        length(Qs, N),
        Qs ins 1..N,
        safe_queens(Qs).

safe_queens([]).
safe_queens([Q|Qs]) :- safe_queens(Qs, Q, 1), safe_queens(Qs).

safe_queens([], _, _).
safe_queens([Q|Qs], Q0, D0) :-
        Q0 #\= Q,
        abs(Q0 - Q) #\= D0,
        D1 #= D0 + 1,
    safe_queens(Qs, Q0, D1).
