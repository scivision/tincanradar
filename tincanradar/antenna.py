#!/usr/bin/env python3
from numpy import log10

def uvm2dbm(uvm,range_m=3.):
    """
    converts microvolts per meter uV/m to dBm in a 50 ohm system

    inputs:
    uvm: microvolts/meter
    r: standoff distance (meters)

    outputs:
    dbm: decibels relative to 1 mW in 50 ohm system

    S = E^2/(120*pi) = P/(4*pi*r^2) #[W/m^2] Power density vs. E-field,power,distance
    P = E^2*r^2/30  # [W] Power vs. E-field,distance
    We are interested in dBm, so we want dBm ~ uV/m
    10*log10(P)    = 10*log10(E^2) + 10*log10(r^2/30) # dBW = dBV + dBfriis
    dBm  -30 = (20*log10(uvm)-120) + 10*log10(r^2/30) # dBm = dBuV + dBfriis
    dBm = 20*log10(uvm) - 120 + 30 + 10*log10(r^2/30)
    Example:
    dBm = 20*log10(uvm) - 95.2287874528 for r=3m (FCC)
    """
    return dbuvm2dbm(20.*log10(uvm),range_m)

def dbuvm2dbm(dbuvm,range_m=3.):
    """
    converts microvolts(dB) per meter dBuV/m to dBm in a 50 ohm system

    inputs:
    dbuvm: microvolts(dB)/meter
    r: standoff distance (meters)

    outputs:
    dBm: decibels relative to 1mW in 50 ohm system
    """
    return dbuvm - 90. + 10.*log10(range_m**2./30.)

