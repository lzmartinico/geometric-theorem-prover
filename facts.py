from theorem_prover import *

def triangle(a,b,c):
	a.x = 0
	a.y = 0
	b.x = add_variable()
	b.y = 0
	c.x = add_variable()
	c.y = add_variable()
	return None

def right_triangle(a,b,c):
	a.x = 0
	a.y = 0
	b.x = add_variable()
	b.y = 0
	c.x = 0
	c.y = add_variable()
	return None

def parallelogram(a,b,c,d):
	a.x = 0
	a.y = 0
	b.x = add_variable()
	b.y = 0
	c.x = add_variable()
	c.y = add_variable()
	d.x = add_variable(False) 
	d.y = add_variable(False)
	h1 = d.x-b.x-c.x
	h2 = d.y-b.y-c.y
	return (h1,h2)

def parallel((a,b), (c,d)):
	return (b.y-a.y)*(d.x-c.x)-(d.y-c.y)*(b.x-a.x)

def perpendicular((a,b),(c,d)):
	return (b.y-a.y)*(d.y-c.y) + (d.x-c.x)*(b.x-a.x)

def collinear(a,n,b):
	return (n.y-a.y)*(b.x-a.x)-(b.y-a.y)*(n.x-a.x)

def equidistant((a,b),(c,d)):
	return (a.x-b.x)**2+(a.y-b.y)**2-(c.x-d.x)**2-(c.y-d.y)**2

def midpoint(a,n,b):
	h1 = (a.x-n.x)**2+(a.y-n.y)**2-(b.x-n.x)**2-(b.y-n.y)**2
	h2 = collinear(a,n,b)
	return (h1,h2)
	return equidistant((a,n),(n,b)) 

def on_circle_radius((a,b),c):
	'''Point c is on circle with radius ab'''
	return equidistant((a,b),(a,c))

def acute_angles_equal((a,b,c),(d,e,f)):
	cos1 = (a.x-b.x)*(c.x-b.x) + (a.y-b.y)*(c.y-b.y)
	cos2 = (d.x-e.x)*(f.x-e.x) + (d.y-e.y)*(f.y-e.y)
	return cos1-cos2

def bisects_angle((a,b,c), d):
	'''Line bd bisects angle abc'''
	return acute_angles_equal((a,b,d),(d,b,c))

def intercept(p,a,b):
    '''Point p is the interception of line tuples a and b'''
    return (collinear(a[0],p,a[1]), collinear(b[0],p,b[1]))

def altitude(a,b,(c,d)):
    '''Point a is the altitude from b on line cd'''
    return perpendicular((a,b),(c,d))
