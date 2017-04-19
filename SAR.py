#!/usr/bin/env python
"""
Noise-free, clutter-free simulation of linear 1-D displacement linear FMCW radar
This sim assume cross-range displacement is small, antenna radiation pattern is hemispherical, so that a spotlight-like mode results

Michael Hirsch
"""
from pathlib import Path
from numpy import arange,hypot,empty,complex128
from matplotlib.pyplot import show
import h5py
#
from tincanradar.fwdmodel import fmcwtransceive
from tincanradar.plots import plotraw,rangemigration
#%% radar parameters

bm = 400e6 # Hz
tm = 0.02 #s
adcbw = 20000 # Hz
adcfs = 48000 # Hz
tfs = 550e6 #Hz #for sim only
nlfm = 0. #0=perfectly linear FMCW sweep
#%% target parameters
xstart = -1.5 #m
xend = 1.5 #m
dx = 0.05 #m

x0,y0 = 0,1.5 #m

fn = 'first.h5' # hdf5 to load or save

def simsar(fn=None):
    Ns = int(tm*adcfs)

    x = arange(xstart,xend,dx,dtype=float)
    y = 0 #1-D linear displacement
    srng = hypot(x-x0,y-y0)
    #%% range to target --> beat frequencies
    # we do this one range at a time (like in real life), but here to conserve RAM when simulating chirp
    s = empty((x.size,Ns),dtype=complex128)
    for i,r in enumerate(srng):
        if not (i % 2): 
            print(f'{i/x.size*100:.1f} %')
        s[i,:],t = fmcwtransceive(bm,tm,r,adcbw,adcfs,tfs,nlfm)

    if fn:
        fn = Path(fn).expanduser()
        with h5py.File(str(fn),'w') as h:
            h.create_dataset('/s',data=s,compression='gzip',shuffle=True,fletcher32=True)
            h['/t'] = t
            h['/x'] = x
            h['/y'] = y
            h['/x0'] = x0
            h['/y0'] = y0
            h['/bm'] = bm
            h['/tm'] = tm
            h['/adcbw']= adcbw
            h['/adcfs']= adcfs

    return s,t,x

def loadsar(fn):
    with h5py.File(fn,'r') as h:
        s = h['/s'].value
        t = h['/t'].value
        x = h['/x'].value
    return s,t,x

def procsar(s,t,x,adcfs,bm):
    plotraw(s,t,x,adcfs,bm)
    rangemigration(s,t,x,adcfs,bm)

if __name__ == '__main__':
    try:
        s,t,x=loadsar(fn)
        procsar(s,t,x,adcfs,bm)
    except OSError:
        s,t,x = simsar(fn)
        procsar(s,t,x,adcfs,bm)

show()
