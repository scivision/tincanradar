from __future__ import division
from numpy import log10,pi,exp,asarray,arange
from scipy.signal import firwin,lfilter,resample
#from matplotlib.pyplot import specgram
#
c = 299792458
a = 1

def friis(range_m,freq,exp=2):
    return 10*log10((4*pi * freq / c)**2 * range_m**exp)

def fmcwtransceive(bm,tm,range_m,adcbw,adcfs,tfs,nlfm=0.):
    """
    Y is complex sinusoids at homodyne output (zero IF)
    t is elapsed time of each sample of Y

    """
    assert adcbw < 2*adcfs,'Nyquist violated on ADC video filter'

    t = arange(0,tm,1/tfs)

    xt,lo = chirp(bm,tm, t, range_m,nlfm)
   # specgram(lo,Fs=tfs)
#%% mixer, lpf
    y = xt * lo.conjugate()

    h = firwin( numtaps=100, cutoff=adcbw, nyq=tfs/2)
    y = lfilter( h, 1., y)

    Y,t = resample(y,int(xt.size * adcfs / tfs),t)
    return Y,t
#%% FMCW
def chirp(bm,tm,t,range_m,nlfm=0.):

    toffs = 2 * asarray(range_m)/c

    if t.size*range_m.size*8 > 8e9:
        raise MemoryError('too much RAM used {:.1e} B'.format(t.size*range_m.size*8))

    lo = 1*exp(1j * chirp_phase(bm,tm,t,nlfm)) # unit amplitude, set transmit power in Prx fwdmodel.py
#%% targets
    xtargs = a * exp(1j*chirp_phase(bm,tm,t+toffs, nlfm))

    return xtargs, lo

def chirp_phase(bm,tm,t,nlfm):

    B1 = bm / tm
    B2 = bm / tm**2
    #2*pi since we specified frequency in Hertz
    #FIXME check 0.5 scalar
    return 2*pi*(-0.5*bm*t  #starting freq
                 + 0.5*B1*t**2    #linear ramp ("derivative of phase is frequency")
                 + 0.5*nlfm*B2*t**3) #quadratic frequency