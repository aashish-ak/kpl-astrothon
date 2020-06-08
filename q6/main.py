# all imports below
import math
import geopy
from geopy.distance import VincentyDistance
#import sympy as sp
"""
Any extra lines of code (if required)
as helper for this function.
"""

def findstrike(velocity, alt, az):
	'''
	Parameters
	----------
	velocity : A `float`
    alt: A `float`
    az: A `float`
	
	Returns
	-------
	A `tuple` of two floats
	'''
 
	everest_height = 8848
	everest_coordinates	=	(27.9881,86.9260)
	vel_ver	=	velocity*math.sin(alt)
	vel_hor	=	velocity*math.cos(alt)


	t_impact	=	vel_ver + math.sqrt(2*9.81*8848+vel_ver*vel_ver)
	t_impact	=	t_impact/9.81
	
	h = 8848
	v = vel_ver
	vh= vel_hor
	d = 0
	t = 0.001
	r =  6400000
	g = -9.81*(1-(2*h/r))
	
	while h>0:
		h = h+v*t
		v = v+g*t
		g = -9.81*(1-(2*h/r))
		d += vh*t 
        
	impact_distance	=	d
	
	
	origin = geopy.Point(everest_coordinates[0], everest_coordinates[1])
	destination = VincentyDistance(kilometers=
		(impact_distance/1000)).destination(origin, az)
		
	return destination[0],destination[1]

findstrike(200,34,213.123)
# x,t = sp.symbols('x t')
# print(x.diff(t))
