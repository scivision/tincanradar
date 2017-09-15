from time import time
import warnings
from numpy import log10,pi,exp,asarray,arange,ndarray
from scipy.signal import firwin,lfilter,resample
try:
    import pychirp as fwd
except ImportError:
    fwd = None
    warnings.warn('falling back to slow non-Fortran method')
#
c = 299792458.
Atarg = [0.2] # target amplitude, arbitrary (and often very small!)

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
        xt,lo = chirprx(bm,tm, t, range_m,nlfm)
        y = xt * lo.conjugate()
        # specgram(lo,Fs=tfs)
    print(f'{time()-tic:.3f} sec to compute time-domain chirp')
#%% mixer lpf
    tic=time()
    h = firwin(numtaps=100, cutoff=adcbw, nyq=tfs/2.)
    y = lfilter(h, 1., y)
    print(f'{time()-tic:.3f} sec to anti-alias filter')

    Y,t = resample(y,int(y.size * adcfs / tfs),t)
    return Y,t

def FMCWnoisepower(NF,adcbw):
    """
    Compute noise power for FMCW radar in dBm
    Note: we are talking power not PSD. Hence we use final ADC filter bandwidth.
    """
    #RXbw = 2/tm # [Hz]

    return -174.4 + NF + 10*log10(adcbw) #[dBm]
# %% FMCW
def chirprx(bm:float, tm:float, t, range_m, Atarg, nlfm:float=0.):
    """
    inputs
    -------
    bm: scalar: bandwidth of chirp [Hz]
    tm: scalar: time length of chirp [sec]
    t: vector of time samples [sec]
    range_m: scalar or vector: target range(s) [m]
    A_targ: scalar or vector:  target amplitude(s) [V]
    nlfm: scalar: chirp non-linearity factor (0. for perfectly linear)

    outputs
    -------
    lo: output of transmitter VCO, YIG, or DAC that is amplified and sent out transmit antenna
    xtargs: ideal reflected signal from targets with round-trip delay.
    """
    lo = chirptx(bm,tm,t,nlfm)
# %% targets
    range_m = asarray(range_m)

    toffs = 2 * range_m/c

    if t.size*range_m.size*8 > 8e9:
        raise MemoryError(f'too much RAM used {t.size*range_m.size*8:.1e} B')

    xtargs = Atarg * chirptx(bm, tm, t+toffs, nlfm)

    return xtargs, lo

def chirptx(bm:float, tm:float, t:ndarray, nlfm:float):

    B1 = bm / tm
    B2 = bm / tm**2
    # 2*pi since we specified frequency in Hertz
    # FIXME check 0.5 scalar
    phase = 2*pi*(-0.5*bm*t            # starting freq
                 + 0.5*B1*t**2.        # linear ramp ("derivative of phase is frequency")
                 + 0.5*nlfm*B2*t**3.)  # quadratic frequency

    lo = 1*exp(1j * phase)  # unit amplitude, set transmit power in Prx fwdmodel.py

    return lo
