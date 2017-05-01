"""
the formation of these plots follow Sec. 4.2 of Greg Charvat "Small and Short-Range Radar Systems" CRC Press 2014

"""
import numpy as np
from matplotlib.pyplot import figure,subplots,clf,draw,pause
#
from . import psd

def plots(t, y, fs, Np):
#%% time domain movie
    fg,axs = subplots(1,2)

    ax = axs[0]
    hr = ax.plot(t[:Np],y[0,:Np])[0]
    ax.set_title('Noisy Sinusoid')
    ax.set_xlabel('time [sec]')
    ax.set_ylabel('amplitude')

    ax = axs[1]
    Pxx,fax = psd(y[0,:Np], fs)
    hp = ax.plot(fax,10*np.log10(Pxx))[0]
    ax.set_title('Noisy PSD')
    ax.set_xlabel('Frequency [Hz]')
    ax.set_ylabel('amplitude [dB]')

    for Y in y:
        hr.set_ydata(Y[:Np])

        Pxx,fax = psd(Y[:Np], fs)
        hp.set_ydata(10*np.log10(Pxx))

        draw(); pause(0.001)

def rangemigration(s,t,x,adcfs,bm):
    #%% Section 4.2 of Greg Charvat "Small and Short-Range radar Systems" CRC Press 2014
    sk = np.fft.fft(s,axis=0)

    fg = figure(46); clf();    ax = fg.gca()
    hi=ax.pcolormesh(abs(sk))
    ax.set_title('Magnitude of Cross range DFT')
    fg.colorbar(hi)

    fg = figure(47); clf();  ax = fg.gca()
    hi=ax.pcolormesh(np.angle(sk))
    ax.set_title('Phase of Cross range DFT')
    fg.colorbar(hi)

def plotraw(s,t,x,fs,bm):
    frf = np.linspace(-bm/2,bm/2,num=s.shape[1])
    #x= append(x,x[-1]+(x[-1]-x[-2]))
    xpc,ypc = np.meshgrid(frf,x)
#%% plot magnitude of returns   Fig. 4.3 Charvat
    fg = figure(43); fg.clf(); ax = fg.gca()
    hi=ax.pcolormesh(xpc,ypc,s.real)
    fg.colorbar(hi)
    ax.set_title('Real Part of IF signal')
    ax.set_ylabel('x-displacement of radar [m]')
    ax.set_xlabel('IF chirp frequency [Hz]')
#%% plot angle of returns       Fig 4.4 Charvat
    fg = figure(44);  clf(); ax = fg.gca()
    hi=ax.pcolormesh(xpc,ypc, np.angle(s))
    fg.colorbar(hi)
    ax.set_title('Angle of IF signal')
    ax.set_ylabel('x-displacement of radar [m]')
    ax.set_xlabel('IF chirp frequency [Hz]')
#%% IDFT along downrange of raw beat frequency data Fig 4.5 Charvat
    fg = figure(45); clf(); ax = fg.gca()
    hi = ax.pcolormesh(xpc,ypc,abs(np.fft.ifft(s,axis=1)))
    fg.colorbar(hi)
    ax.set_title('Relative ranges from IDFT(IF signal) along downrange dimension')
    ax.set_ylabel('x-displacement of radar [m]')
    ax.set_xlabel('relative range')
