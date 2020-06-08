# all imports below
import math as m
import numpy as np
import astropy.units as u
#from scipy.constants import light_year, parsec
"""
Any extra lines of code (if required)
as helper for this function.
"""

def findDistance(vrec):
    '''
    Parameters
    ----------
    vrec : a `float`
    
    Returns
    -------
    a `float`
    '''
    # a = (np.float128)(vrec/(71))*(m.pow(10,6))*parsec
    # a = (a/(light_year))*u.lyr
    a = (np.float128)(vrec/(71))*(u.Mpc).to(u.lyr)
    return a
