# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 12:23:32 2022

@author: Conner Onstenk
"""

import math
import numpy as np

def ecef_to_lla():
    '''
    

    Returns
    -------
    None.

    '''
    pass

def lla_to_ecef(lla):
    '''
    

    Parameters
    ----------
    lla : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    '''
    '''
    Convert latitude, longitude, and altitude to cartesian Earth Centered 
    Earth Fixed (ECEF) coordinates assuming a spherical Earth
    
    Input:
        lla:    n x 3 numpy array with columns representing lat/lon/alt 
                [deg, deg, km]
        
    Output:
        ecef:   n x 3 numpy array with columns representing x/y/z dimensions of
                an ECEF coordinate frame [km, km, km]
    '''
    r = lla[:,2] + 6378
    ecefx = r * np.cos(lla[:,1]*math.pi/180) * np.sin(lla[:,0]*math.pi/180)
    ecefy = r * np.sin(lla[:,1]*math.pi/180) * np.sin(lla[:,0]*math.pi/180)
    ecefz = r * np.cos(lla[:,0]*math.pi/180)
    return np.column_stack((ecefx, ecefy, ecefz))

def ecef_to_eci(ecef, datetime):
    '''
    ecef_to_eci converts Earth Centered Earth Fixed (ECEF) coordinates at a 
    specified datetime to Earth Centered Inertial (ECI) coordinates. Units of
    ECI output will match the units of the ECEF input

    Parameters
    ----------
    ecef : numpy array
        n x 3 numpy array with columns representing x/y/z dimensions of an ECEF
        coordinate frame
    datetime : datetime object
        Datetime at which the ecef coordinates are to be represented

    Returns
    -------
    eci : numpy array
        n x 3 numpy array with columns representing x/y/z dimensions of an ECI
        coordinate frame

    '''
    pass

def eci_to_ecef(eci, datetime):
    '''
    eci_to_ecef converts Earth Centered Inertial (ECI) coordinates at a 
    specified datetime to Earth Centered Earth Fixed (ECEF) coordinates. Units
    of ECEF output will match the units of the ECI input

    Parameters
    ----------
    eci : numpy array
        n x 3 numpy array with columns representing x/y/z dimensions of an ECI
        coordinate frame
    datetime : datetime object
        Datetime at which the ecef coordinates are to be represented

    Returns
    -------
    ecef : numpy array
        n x 3 numpy array with columns representing x/y/z dimensions of an ECEF
        coordinate frame

    '''
    pass

def aer_from_lla(lla_viewer, lla_target):
    '''
    

    Parameters
    ----------
    lla_viewer : 1 x 3 numpy array
        Latitude [deg], longitude [deg], and altitude [km] of source location 
        the azimuth, elevation, and range values are calculated from
    lla_target : n x 3 numpy array
        Latitude [deg], longitude [deg], and altitude [km] of target 
        location(s) the azimuth,  elevation, and range values are calculated to

    Returns
    -------
    aer : n x 3 numpy array [deg, deg, km]
        Azimuth [deg], elevation[deg], and range [km] from the viewer to each
        of the provided target locations

    '''
    pass


if __name__ == '__main__':
    lla = np.array([[0, 45, 6378], [90, 45, 23378]])
    ecef = lla_to_ecef(lla)
