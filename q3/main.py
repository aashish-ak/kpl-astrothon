# all imports below

"""
Any extra lines of code (if required)
as helper for this function.

Gravitational Time Dilation = sqrt( 1 - ( 2*G*M / (dist-R)*(c**2) ) ) * (nano secs in a day)
(after approximation, we are interested in finding the diff between earth and the satellite) 
delta(1/gamma) = GM/R(c**2) - GM/dist(c**2)
Time dilation = nanosecs in a day * delta(1/gamma)
"""

def findDelay(dist):
	'''
	Parameters
	----------
	dist : A `float`
	
	Returns
	-------
	A `float`
	'''
	R = 6357000 # in SI units
	# Simplified to GM/c^2(1/R - 1/dist)
	delta_gamma = ( (6.674 * 5.974) / (2.998**2) ) * ((1.0/R) - (1.0/dist))
        nanosecs_in_a_day = 24*60*60*(10**6) # divided by 10**3 due to c^2 computation above
	
	return delta_gamma*nanosecs_in_a_day

