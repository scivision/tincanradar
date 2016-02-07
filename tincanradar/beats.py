#!/usr/bin/env python3
"""
Computes the min/max FMCW beat frequency expected for a given range vs. sweep time and RF bandwidth

You might consider planning your sweep frequency and beat frequencies to land within the range of a PC sound card, say 200Hz - 24kHz
(I try to avoid 60,120,180Hz for powerline harmonics)

Refs:
1) D. G. Luck, Frequency Modulated Radar. New York: McGraw-Hill, 1949.
2) M. Hirsch. “A Low-Cost Approach to L-band FMCW Radar: Thru-Wall Microwatt Radar". Ottawa, Ontario: North American Radio Science Meeting, July 2007.
"""
from __future__ import division
from numpy import asarray

c = 299792458

def range2beat(range_m, fm, bw):
    """
    range_m: one-way range to target in meters
    bw: FMCW linear chirp bandwidth
    fm: cadence of sweep (how many sweeps/sec,  or 1/tm)
    """
    return 2*asarray(range_m)*bw*fm/c

def beat2range(beats,fm,bw):
    """
    beats: beat frequencies from target returns
    bw: FMCW linear chirp bandwidth
    fm: cadence of sweep (how many sweeps/sec,  or 1/tm)
    """
    return c * beats /(2*bw*fm) #distance estimate, meters


def bw2rangeres(bw):
    return c/(2*bw)


if __name__ == '__main__':
    from argparse import ArgumentParser
    p = ArgumentParser(description='calculate beat frequencies returned by stationary point targets via FMCW stimulus')
    p.add_argument('-r','--range',help='range(s) to point target [meters]',type=float,nargs='+',default=[1,10,50])
    p.add_argument('--fm',help='sweep frequency [Hz], a.k.a. 1/tm',type=float,default=100)
    p.add_argument('-b','--bw',help='RF bandwidth [Hz] over which you sweep e.g. 10.2 GHz - 10.7 GHz is 500e6',type=float,default=500e6)
    p = p.parse_args()

    fb = range2beat(p.range,p.fm,p.bw)

    rngres = bw2rangeres(p.bw)

    print('For point target ranges {} meters you may expect beat tones {} Hz.'.format(p.range,['{:.1f}'.format(f) for f in fb]))
    print('Using {} MHz RF bandwidth, you may expect {:.4f} meters range resolution.'.format(p.bw/1e6,rngres))
