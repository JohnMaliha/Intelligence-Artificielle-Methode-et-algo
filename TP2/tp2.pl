% Exercice 3.7
homme(hugo).
homme(loic).
homme(gabriel).
homme(maxime).
homme(mathieu).
homme(alexis).

femme(catherine).
femme(justine).
femme(lea).
femme(alice).
femme(rose).
femme(emma).

parent(hugo, lea).
parent(hugo, gabriel).

parent(catherine, lea).
parent(catherine, gabriel).

parent(loic, alice).
parent(loic, maxime).
parent(loic, mathieu).

parent(justine, alice).
parent(justine, maxime).
parent(justine, mathieu).

parent(gabriel, alexis).
parent(gabriel, rose).
parent(gabriel, emma).

parent(alice, alexis).
parent(alice, rose).
parent(alice, emma).

enfant(X,Y) :- parent(Y,X).
fille(X,Y) :- parent(Y,X), femme(X).
fils(X,Y) :- parent(Y,X), homme(X).
mere(X,Y) :- parent(X,Y), femme(X).
pere(X,Y) :- parent(X,Y), homme(X).
frere(X,Y) :- pere(Z,X), pere(Z,Y), homme(X), X\=Y.
soeur(X,Y) :- pere(Z,X), pere(Z,Y), femme(X), X\=Y.
oncle(X,Y) :- frere(X,Z), parent(Z,Y).
tante(X,Y) :- soeur(X,Z), parent(Z,Y).
grand_parent(X,Y) :- parent(X,Z), parent(Z,Y).
grand_pere(X,Y) :- grand_parent(X,Y), homme(X).
grand_mere(X,Y) :- grand_parent(X,Y), femme(X).
petit_enfant(X,Y) :- grand_parent(Y,X).
petite_fille(X,Y) :- petit_enfant(X,Y), femme(X).
petit_fils(X,Y) :- petit_enfant(X,Y), homme(X).


% Exercice 4.3.1
sum(X,Y,R) :- R is X+Y.

% Exercice 4.3.2
max2(X,Y,M) :- X>Y -> M is X; M is Y.

% Exercice 4.3.3
max3(X,Y,Z,M) :- max2(X,Y,R), max2(R,Z,M).

% Exercice 4.5
mot(abalone, a,b,a,l,o,n,e).
mot(abandon, a,b,a,n,d,o,n).
mot(enhance, e,n,h,a,n,c,e).
mot(anagram, a,n,a,g,r,a,m).
mot(connect, c,o,n,n,e,c,t).
mot(elegant, e,l,e,g,a,n,t).

crossword(H1,H2,H3,V1,V2,V3) :- 
    mot(H1, _,H1V1,_,H1V2,_,H1V3,_), 
    mot(H2, _,H2V1,_,H2V2,_,H2V3,_), 
    mot(H3, _,H3V1,_,H3V2,_,H3V3,_), 

    mot(V1, _,H1V1,_,H2V1,_,H3V1,_), 
    mot(V2, _,H1V2,_,H2V2,_,H3V2,_), 
    mot(V3, _,H1V3,_,H2V3,_,H3V3,_).

% Exercice 4.8
max([],0).
max([H|T], M) :- max(T, M1), max2(H, M1, M).

somme([],0).
somme([H|T],S) :- somme(T, S1), S is S1+H.

nth(1,[H|_], H).
nth(N, [_|T], R) :- N1 is N-1, nth(N1, T, R).

zip([H1],[H2],[[H1,H2]]).
zip([H1|T1], [H2|T2], R) :- zip(T1,T2,R1), append([[H1,H2]], R1, R).

enumerate(0, []).
enumerate(N,L) :- N > 0, N1 is N-1, enumerate(N1, L1), append(L1, [N1], L).

% Bonus
rend_monnaie(Argent,Prix) :-
    write('A rendre :'), nl,
    trouver_piece(Argent - Prix, [2, 1, 0.25, 0.10, 0.05] ).

trouver_piece(Change,[Piece|Pieces]) :-
    NbrPiece is floor(Change/Piece),
    NouveauChange is Change - NbrPiece*Piece,
    write(NbrPiece), write(' piece de '), write(Piece), nl, 
    trouver_piece(NouveauChange,Pieces).