#!/usr/bin/env python
"""
Computes the min/max FMCW beat frequency expected for a given range vs. sweep time and RF bandwidth

You might consider planning your sweep frequency and beat frequencies to land within the range of a PC sound card, say 200Hz - 24kHz
(I try to avoid 60,120,180Hz for powerline harmonics)

Refs:
1) D. G. Luck, Frequency Modulated Radar. New York: McGraw-Hill, 1949.
2) M. Hirsch. “A Low-Cost Approach to L-band FMCW Radar: Thru-Wall Microwatt Radar". Ottawa, Ontario: North American Radio Science Meeting, July 2007.
"""
import numpy as np
from scipy.constants import c

def range2beat(range_m, tm:float, bw:float):
    """
    range_m: one-way range to target in meters
    bw: FMCW linear chirp bandwidth
    tm: time of sweep
    """
    return 2*np.asarray(range_m)*bw/(tm*c)

def beat2range(beats, tm:float, bw:float):
    """
    beats: beat frequencies from target returns
    bw: FMCW linear chirp bandwidth
    tm: time of sweep
    """
    return c * beat2time(beats,tm,bw) #distance estimate, meters

def beat2time(beats, tm:float, bw:float):
    return beats*tm / (2*bw) #two-way travel time, seconds

def bw2rangeres(bw):
    return c / (2*bw)

def beatlinear1d(x, y, tm:float, bw:float):
    """
    returns linear FMCW beat frequencies as a result of 1-D displacement x, perpendicular distance y from radar antenna
    x: vector of x-displacement [m]
    y: distance from radar
    tm: time of sweep
    bw: FMCW linear chirp bandwidth

    """
    #theta = np.angle1d(x,y)
    srng = np.hypot(x,y)

    return range2beat(srng, tm,bw)


def angle1d(x, y):
    """
    returns angles due to 1-D displacement in x relative to a reference at position y
    right triangle geometry
    """

    return np.degrees(np.arctan(y/x))

def simtone(tm, fs, SNR, Ftone, Nobs):
    t = np.arange(0,tm,1/fs) #time samples
    x = np.sqrt(2)* np.exp(1j*2*np.pi*Ftone*t) #noise-free signal

    nvar = 10**(-SNR/10.) #variance of noise
    noise = np.sqrt(nvar)*(np.random.randn(Nobs,x.size) + 1j*np.random.randn(Nobs,x.size))

    print('SNR measured {:.1f} dB'.format(snrest(x,noise[0,:])))

    y = x + noise #noisy observation

    return t, y

def uvm2dbm(uvm, range_m=3.):
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
    return dbuvm2dbm(20. * np.log10(uvm),range_m)

def dbuvm2dbm(dbuvm, range_m=3.):
    """
    converts microvolts(dB) per meter dBuV/m to dBm in a 50 ohm system

    inputs:
    dbuvm: microvolts(dB)/meter
    r: standoff distance (meters)

    outputs:
    dBm: decibels relative to 1mW in 50 ohm system
    """
    return dbuvm - 90. + 10. * np.log10(range_m**2./30.)
# %% estimation
def rssq(x, axis=None):
    """
    root-sum-of-squares
    """
    x = np.asarray(x)
    return np.sqrt(ssq(x,axis))

def ssq(x, axis=None):
    """
    sum-of-squares
        this method is ~10% faster than (abs(x)**2).sum()
    """
    x = np.asarray(x)
    return(x*x.conj()).real.sum(axis)


def snrest(noisy, noise, axis=None):
    """
    Computes SNR [in dB] when you have:
    "noisy" signal+noise time series
    "noise": noise only without signal
    """

    Psig   = ssq(noisy,axis)
    Pnoise = ssq(noise)

    return 10 * np.log10(Psig/Pnoise) # SNR in dB

def psd(x, fs:int, zeropadfact:float=1, wintype=np.hanning):
    """
    https://www.mathworks.com/help/signal/ug/psd-estimate-using-fft.html
    take 10*log10(Pxx) for [dB/Hz]
    """
    nt = x.size

    win = wintype(nt)

    nfft = int(zeropadfact * nt)

    X = np.fft.fft(win * x, nfft, axis=-1)
    X = X[:nfft//2]

    Pxx = 1./(fs*nfft) * abs(X)**2.
    Pxx[1:-1] = 2*Pxx[1:-1] #scales DC appropriately

    f = np.arange(0.,fs/2.,fs/nfft)[:Pxx.size] # shifted fft freq. bins

    return Pxx, f
