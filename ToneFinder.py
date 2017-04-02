#!/usr/bin/env python
"""
Simulates noisy sinusoids
"""
from tincanradar import simtone
from tincanradar.plots import plots

Nobs = 100
fs = 16000
tm = 0.1
Ftone = 1000. #[Hz]
SNR = 20 #[dB]
Np = 200 #points to plot
#
Ns = int(tm*fs)


if __name__ == '__main__':
    t,y = simtone(tm,fs,SNR,Ftone,Nobs)
    plots(t,y,fs,Np)

