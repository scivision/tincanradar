#!/usr/bin/env python
from numpy import iscomplex
from numpy.testing import run_module_suite,assert_allclose
#
from tincanradar import simtone
from tincanradar.estimation import snrest
#
Nobs = 1
fs = 16000.
tm = 0.1
Ftone = 1000. #[Hz]
SNR = 50. #[dB]

def test_simtone():
    t,y = simtone(tm,fs,SNR,Ftone,Nobs)
    assert iscomplex(y).any()

def test_snrest():
    sig = [1,-1]
    noise = [0.1,-0.1]
    snr = snrest(sig+noise, noise)
    assert_allclose(snr, 20., rtol=.1)

if __name__ == '__main__':
    run_module_suite()
