#!/usr/bin/env python3
"""
"""
from numpy.random import randn
from numpy import arange,exp,pi,sqrt
from matplotlib.pyplot import figure,show,draw,pause
from numpy.fft import fft
#
from tincanradar.estimation import snrest

Nobs = 100
fs = 48000
tm = 0.1
Ftone = 1000. #[Hz]
SNR = 20 #[dB]
Np = 200 #points to plot
#
Ns = int(tm*fs)

def simtone():
    t = arange(0,tm,1/fs) #time samples
    x = sqrt(2)*exp(1j*2*pi*Ftone*t) #noise-free signal

    nvar = 10**(-SNR/10.) #variance of noise
    noise = sqrt(nvar)*(randn(Nobs,x.size) + 1j*randn(Nobs,x.size))

    print('SNR measured {} dB'.format(snrest(x,noise[0,:])))

    y = x + noise #noisy observation

    return t,y

def plots(t,y):
#%% time domain movie
    fg = figure(1); fg.clf()
    ax = fg.gca()
    hp = ax.plot(t[:Np],y[0,:Np])[0]
    ax.set_title('Noisy Sinusoid')
    ax.set_xlabel('time [sec]')
    ax.set_ylabel('amplitude')
    for Y in y:
        hp.set_ydata(Y[:Np])
        draw(); pause(0.001)

#%% PSD movie
    fg = figure(2); fg.clf()
    ax = fg.gca()


if __name__ == '__main__':
    t,y = simtone()
    plots(t,y)
