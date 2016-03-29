from __future__ import division
from time import time
from numpy import log10,pi,exp,asarray,arange
from scipy.signal import firwin,lfilter,resample
try:
    import fwd
except ImportError:
    fwd = None

#
c = 299792458.
Atarg = [0.2]

def friis(range_m,freq,exp=2):
    return 10*log10((4*pi * freq / c)**2 * range_m**exp)

def fmcwtransceive(bm,tm,range_m,adcbw,adcfs,tfs,nlfm=0.):
    """
    Y is complex sinusoids at homodyne output (zero IF)
    t is elapsed time of each sample of Y

    """
    assert adcbw < 2*adcfs,'Nyquist violated on ADC video filter'

    t = arange(0,tm,1/tfs)

    tic = time()
    if fwd is not None:
        y = fwd.fwdmodel.chirp(bm,tm, t, range_m, Atarg, nlfm)
    else:
        xt,lo = chirp(bm,tm, t, range_m,nlfm)
        y = xt * lo.conjugate()
        # specgram(lo,Fs=tfs)
    print('{:.3f} sec to compute time-domain chirp'.format(time()-tic))
#%% mixer lpf
    tic=time()
    h = firwin( numtaps=100, cutoff=adcbw, nyq=tfs/2)
    y = lfilter( h, 1., y)
    print('{} sec to anti-alias filter'.format(time()-tic))

    Y,t = resample(y,int(y.size * adcfs / tfs),t)
    return Y,t
#%% FMCW
def chirp(bm,tm,t,range_m, Atarg, nlfm=0.):

    toffs = 2 * asarray(range_m)/c

    if t.size*range_m.size*8 > 8e9:
        raise MemoryError('too much RAM used {:.1e} B'.format(t.size*range_m.size*8))

    lo = 1*exp(1j * chirp_phase(bm,tm,t,nlfm)) # unit amplitude, set transmit power in Prx fwdmodel.py
#%% targets
    xtargs = Atarg * exp(1j*chirp_phase(bm,tm,t+toffs, nlfm))

    return xtargs, lo

def chirp_phase(bm,tm,t,nlfm):

    B1 = bm / tm
    B2 = bm / tm**2
    #2*pi since we specified frequency in Hertz
    #FIXME check 0.5 scalar
    return 2*pi*(-0.5*bm*t  #starting freq
                 + 0.5*B1*t**2    #linear ramp ("derivative of phase is frequency")
                 + 0.5*nlfm*B2*t**3) #quadratic frequency