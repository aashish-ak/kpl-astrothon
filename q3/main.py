# all imports below

"""
Any extra lines of code (if required)
as helper for this function.

Gravitational Time Dilation = 1 - sqrt( 1 - ( 2*G*M / (dist-R)*(c**2) ) ) * (nano secs in a day)
1/gamma = sqrt(1-2GM/R(c**2))
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
	twoGM_by_c_sq = (2*6.674*5.974)/(2.998*2.998*1000)
        one_by_gamma = sqrt( 1 - twoGM_by_c_sq/(dist-R))
        nanosecs_in_a_day = 24*60*60*(10**9)
	
	return (1 - one_by_gamma)*nanosecs_in_a_day

