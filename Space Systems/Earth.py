# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 18:30:42 2022

@author: daisy
"""

import numpy as np
import math

a = 6378137.0
b = 6356752.314140


def calc_ellipsoid_radius(lat):
    '''
    calc_ellipsoid_radius calculates the radius at a specified latitude for the
    WGS84 ellipsoid

    Returns
    -------
    None.

    '''
    lat = lat/180*math.pi
    r = (a**2 * np.cos(lat)**2 + b**2 * np.sin(lat)**2) / \
        (a * np.cos(lat)**2 + b * np.sin(lat)**2)
    return r
        