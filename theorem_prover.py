from sage.all import *

u_variables = []
x_variables = []
statements = []

class Point():
    ui = 0
    xi = 0
    TheoremRing = PolynomialRing(CC, names=[])

def add_variable(arbitrary=True):
    newvar = None
    if arbitrary:
        Point.ui += 1
        newvar = 'u'+str(Point.ui)
        u_variables.append(newvar)
	Point.TheoremRing = PolynomialRing(CC, names=x_variables+u_variables)
    else:
        Point.xi += 1
        newvar = 'x'+str(Point.xi) 
        x_variables.append(newvar)
	Point.TheoremRing = PolynomialRing(CC, names=u_variables+x_variables)
    return Point.TheoremRing.gens()[-1]    

def fact(f, *args):
    stat = f(*args)
    if stat:
        if isinstance(stat, tuple):
	     statements.extend(stat)
	else:
	     statements.append(stat)

def degenerate_conclusion(c, *args):
    Point.TheoremRing = PolynomialRing(CC, names=x_variables+u_variables+['y'])
    y = Point.TheoremRing.gens()[-1]
    if isinstance(c(*args),tuple):
    	I = Ideal(statements + [1-c(*args)[0]*y, 1-c(*args)[1]*y]);	
    else:
        I = Ideal(statements + [1-c(*args)*y])
    if I.groebner_basis() == [1]:
        return True
    return False

def conclusion(c, *args):
    if degenerate_conclusion(c,*args):
        return True
    else:
        F = PolynomialRing(CC,names=u_variables).fraction_field()
        R = PolynomialRing(F, names=x_variables+['y'])
        y = R.gens()[-1]
        if isinstance(c(*args),tuple):
            I = Ideal(statements + [1-c(*args)[0]*y, 1-c(*args)[1]*y]);	
        else:
	    I = R.ideal(statements + [1-c(*args)*y], coerce=True)
#        print I.groebner_basis()
        if 1 in I:#I.groebner_basis() == [1]:
            return True
        return False
