"""
Compute linear 1-D displacement angles
Michael Hirsch
"""
from numpy import degrees, arctan, hypot
#
from .beats import range2beat


def beatlinear1d(x,y):
    """
    returns linear FMCW beat frequencies as a result of 1-D displacement x, perpendicular distance y from radar antenna
    x: vector of x-displacement [m]
    y: distance from radar
    """
    #theta = angle1d(x,y)
    srng = hypot(x,y)

    return range2beat(srng,fm,bw)


def angle1d(x,y):
    """
    returns angles due to 1-D displacement in x relative to a reference at position y
    right triangle geometry
    """

    return degrees(arctan(y/x))
