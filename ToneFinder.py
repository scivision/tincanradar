#!/usr/bin/env python3
"""
"""
from numpy.random import randn
from numpy import arange,exp,pi,sqrt,log10
from matplotlib.pyplot import figure,subplots,draw,pause
#
from tincanradar.estimation import snrest,psd

Nobs = 100
fs = 16000
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
    fg,axs = subplots(1,2)

    ax = axs[0]
    hr = ax.plot(t[:Np],y[0,:Np])[0]
    ax.set_title('Noisy Sinusoid')
    ax.set_xlabel('time [sec]')
    ax.set_ylabel('amplitude')

    ax = axs[1]
    Pxx,fax = psd(y[0,:Np],fs)
    hp = ax.plot(fax,10*log10(Pxx))[0]
    ax.set_title('Noisy PSD')
    ax.set_xlabel('Frequency [Hz]')
    ax.set_ylabel('amplitude [dB]')

    for Y in y:
        hr.set_ydata(Y[:Np])

        Pxx,fax = psd(Y[:Np],fs)
        hp.set_ydata(10*log10(Pxx))

        draw(); pause(0.001)


if __name__ == '__main__':
    t,y = simtone()
    plots(t,y)
