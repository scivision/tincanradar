#!/usr/bin/env python
"""
Simulates chirp transmission without noise
"""
from numpy import arange
from matplotlib.pyplot import figure,show
#
from tincanradar.fwdmodel import chirptx

bm = 0.3e6 # Hz
tm = 0.1 #s
tfs = 1e6 #Hz #for sim only

t = arange(0,tm,1/tfs)

#%% raw chirp waveform centered at IF frequency (here, it's 0)
sig = chirptx(bm,tm,t,nlfm=0.)
#%% Plot power spectral density (PSD)

#f, t, Sxx = spectrogram(sig, tfs)
#ax.pcolormesh(t, f, Sxx)

fg = figure()
ax = fg.gca()
hi=ax.specgram(sig,Fs=tfs,
               vmin=-100)[-1]
ax.set_ylabel('Frequency [Hz]')
ax.set_xlabel('Time [sec]')
ax.set_title('Chirp PSD (centered on LO frequency)')
fg.colorbar(hi,ax=ax)


show()