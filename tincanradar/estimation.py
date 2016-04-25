from numpy import sqrt,asarray,log10,arange
from numpy import hanning as hann
from numpy.fft import fft

def rssq(x,axis=None):
    """
    root-sum-of-squares
    """
    x = asarray(x)
    return sqrt(ssq(x,axis))

def ssq(x,axis=None):
    """
    sum-of-squares
        this method is ~10% faster than (abs(x)**2).sum()
    """
    x=asarray(x)
    return(x*x.conj()).real.sum(axis)


def snrest(noisy,noise,axis=None):
    """
    Computes SNR [in dB] when you have:
    "noisy" signal+noise time series 
    "noise": noise only without signal
    """

    Psig   = ssq(noisy,axis)
    Pnoise = ssq(noise)

    return 10 * log10(Psig/Pnoise) # SNR in dB

def psd(x,fs,zeropadfact=1):
    nt = x.size

    win = hann(nt)

    nfft = int(zeropadfact * nt)

    Fb = fft(win * x, nfft,axis=-1)
    Fb = Fb[:nfft/2]

    Pxx = 2/(fs*nfft) * abs(Fb)**2

    fax = arange(0,fs/2,fs/nfft)[:Pxx.size] #frequencies corresponding to shift fft freq bins

    return Pxx,fax
