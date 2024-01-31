from numpy import iscomplex
from pytest import approx
from tincanradar import simtone, snrest


Nobs = 1
fs = 16000.0
tm = 0.1
Ftone = 1000.0  # [Hz]
SNR = 50.0  # [dB]


def test_simtone():
    t, y = simtone(tm, fs, SNR, Ftone, Nobs)
    assert iscomplex(y).any()


def test_snrest():
    sig = [1, -1]
    noise = [0.1, -0.1]
    snr = snrest(sig + noise, noise)
    assert snr == approx(20.0, rel=0.1)
