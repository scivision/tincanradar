from __future__ import division
from numpy import log10,pi

c = 299792458

def friis(range_m,freq):
    return 20*log10(4*pi * range_m * freq / c)