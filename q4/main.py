# all imports below
import datetime
import ephem
from math import degrees

"""
Any extra lines of code (if required)
as helper for this function.
"""

startobs = datetime.datetime(2020, 6, 8, 18, 39, 4)#replace it by the time when Saturn will be just visible
endobs = datetime.datetime(2020, 6, 9, 1, 11, 42) #replace it by the time when Saturn is no longer visible from SAC terrace



azst = 130.8536
altst = 20.0005

azend = 229.1408
altend = 20.0013

def findSaturn(obstime):
    obstime = obstime - datetime.timedelta(0,19800)
    saturn = ephem.Saturn()
    gravity = ephem.Observer()
    gravity.lat = '31.781300'
    gravity.lon = '76.994110'
    gravity.elev = 1000
    gravity.horizon = '20'
    gravity.date = obstime
    saturn.compute(gravity)
    return (degrees(saturn.az), degrees(saturn.alt))



findSaturn(startobs)

if __name__ == "__main__":
    
    print('Enter your observation in the following format, along with yhe symbols (Do not include trailling zeros) : YYYY/MM/DD HH:MM:DD')
    obstime = input()
    obstime = datetime.datetime.strptime(obstime, '%Y/%m/%d %H:%M:%S')
    obstime = obstime - datetime.timedelta(0,19800)
    temp1 = startobs + datetime.timedelta(0,19800)
    temp2 = endobs +datetime.timedelta(0,19800)
    print('Observation start time =', temp1)
    print('Observation start time =', temp2)
    out = findSaturn(obstime)
    # Uncomment to test on the training data
    print('az = ',out[0])
    print('alt = ',out[1])
    
