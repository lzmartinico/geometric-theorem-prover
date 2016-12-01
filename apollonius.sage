from theorem_prover import *
from facts import *
A = Point()
B = Point()
C = Point()
fact(right_triangle,A,B,C)

M1 = Point()
M1.x = add_variable(arbitrary=False)
M1.y = 0
M2 = Point()
M2.x = 0
M2.y = add_variable(arbitrary=False)
M3 = Point(arbitrary=False)
fact(midpoint,A,M1,B)
fact(midpoint,A,M2,C)
fact(midpoint,B,M3,C)
H = Point(arbitrary=False)
fact(perpendicular,(A,H),(B,C))
fact(collinear,B,H,C)
O = Point(arbitrary=False)
fact(equidistant,(M1,O),(M2,O))
fact(equidistant,(M1,O),(M3,O))
print conclusion(on_circle_radius,(O,H),M1)
print conclusion(on_circle_radius,(O,H),M2)
print conclusion(on_circle_radius,(O,H),M3)
