from numpy import sqrt,asarray,log10

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
    return(x*x.conj()).real.sum(axis)


def snrest(signal,noise,axis=None):
    """
    Computes SNR [in dB] when you have a sample time series with desired signal + noise "signal"
    and also a sample time series without the signal "noise".
    """

    Psig   = ssq(signal,axis)
    Pnoise = ssq(noise)

    return 10 * log10(Psig/Pnoise) # SNR in dB