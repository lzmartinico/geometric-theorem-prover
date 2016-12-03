from theorem_prover import *
from facts import *

A = Point()
A.x = 0
A.y = 0
B = Point()
B.x = add_variable()
B.y = 0
C = Point()
C.x = add_variable()
C.y = 0
Ai = Point()
Ai.x = add_variable()
Ai.y = add_variable()
Bi = Point()
Bi.x = add_variable()
Bi.y = add_variable()
Ci = Point()
Ci.x = add_variable()
Ci.y = add_variable()
fact(collinear, Ai,Bi,Ci)
P = Point(arbitrary=False)
Q = Point(arbitrary=False)
R = Point(arbitrary=False)
fact(intercept,P,(A,Bi),(Ai,B))
fact(intercept,Q,(A,Ci),(Ai,C))
fact(intercept,R,(C,Bi),(Ci,B))
print conclusion(collinear,P,Q,R)
