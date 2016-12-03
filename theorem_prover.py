from sage.all import *

u_variables = []
x_variables = []
statements = []

class Point():
    ui = 0
    xi = 0
    TheoremRing = PolynomialRing(QQ, names=[])
    def __init__(self,arbitrary=True):
        if not arbitrary:
	    self.x = add_variable(arbitrary=False)
	    self.y = add_variable(arbitrary=False)

def add_variable(arbitrary=True):
    newvar = None
    if arbitrary:
        Point.ui += 1
        newvar = 'u'+str(Point.ui)
        u_variables.append(newvar)
	Point.TheoremRing = PolynomialRing(QQ, names=x_variables+u_variables)
    else:
        Point.xi += 1
        newvar = 'x'+str(Point.xi) 
        x_variables.append(newvar)
	Point.TheoremRing = PolynomialRing(QQ, names=u_variables+x_variables)
    return Point.TheoremRing.gens()[-1]    

def fact(f, *args):
    stat = f(*args)
    if stat:
        if isinstance(stat, tuple):
	     for i in stat:
	         if i == 0:
		     continue
		 factored = 1
	         for f in i.factor():
                     if f[0] not in i.parent().gens():
	                 factored *= f[0]
	         statements.append(factored)
	else:
	     factored = 1
	     for f in stat.factor():
                 if f[0] not in stat.parent().gens():
	             factored *= f[0]
	     statements.append(factored)

def degenerate_conclusion(c, *args):
    R = PolynomialRing(CC, names=x_variables+u_variables+['y'])
    y = R.gens()[-1]
    if isinstance(c(*args),tuple):
	conclusions = [1-g*y for g in c(*args)]
	I = R.ideal(statements + conclusions);
    else:
        I = R.ideal(statements + [1-c(*args)*y])
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
	    conclusions = [1-g*y for g in c(*args)]
	    I = R.ideal(statements + conclusions, coerce=True)
        else:
	    I = R.ideal(statements + [1-c(*args)*y], coerce=True)
        if I.groebner_basis() == [1]:
            return True
        return False
