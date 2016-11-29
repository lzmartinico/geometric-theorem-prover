from theorem_prover import *
from facts import *
A = Point()
B = Point()
C = Point()
D = Point()

fact(parallelogram,A,B,C,D)
#fact(parallel, (A,B), (C,D))
#fact(parallel, (A,C), (B,D))

N = Point()
N.x = add_variable(False)
N.y = add_variable(False)
fact(collinear,A,N,D)
fact(collinear,B,N,C)
print conclusion(midpoint,A,N,D)
print conclusion(midpoint,B,N,C)
