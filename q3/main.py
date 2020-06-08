"""
q3-Time-Dilation
Gen. Relativity:
Gravitational Time Dilation = sqrt( 1 - ( 2*G*M / R*(c**2) ) ) * (nano secs in a day)

(after approximation, we are interested in finding the diff between earth and the satellite)

delta(1/gamma) = GM/R(c**2) - GM/dist(c**2) (General Relativity -> Gravity)

Time dilation = nanosecs in a day * delta(1/gamma) 

Special Relativity (for rel. velocity) ---> Add to delta_gamma = -(v^2) / (2*c^2)
where (v^2) / (2*(c^2)) = GM/(c*dist)^2
"""

def findDelay(dist):
    '''
    Parameters
    ----------
    dist : A `float`
	
    Returns
    ----------
    A `float`
    '''
    R = 6357000 # in SI units
    # Simplified to GM/c^2(1/R - 1/dist)
    delta_gamma = ( (6.674 * 5.974) / (2.998**2) ) * ((1.0/R) - (1.0/dist))
    sp_rel = (6.674 * 5.974)/ (2*2.998*2.998*dist)
    #print(sp_rel)
    #print(delta_gamma)
    nanosecs_in_a_day = 24*60*60*(10**6) # divided by 10**3 due to c^2 computation above
	
    return (delta_gamma-sp_rel)*nanosecs_in_a_day

