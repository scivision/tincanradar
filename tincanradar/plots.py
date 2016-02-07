from numpy import arange,linspace,angle,meshgrid
from matplotlib.pyplot import figure


def plotsar(s,t,x,fs,bm):
    frf = linspace(-bm/2,bm/2,num=s.shape[1])
    #x= append(x,x[-1]+(x[-1]-x[-2]))
    xpc,ypc = meshgrid(frf,x)
#%% plot magnitude of returns
    fg = figure()
    ax = fg.gca()
    hi=ax.pcolormesh(xpc,ypc,s.real)
    fg.colorbar(hi)
    ax.set_title('Real Part of IF signal')
    ax.set_ylabel('x-displacement of radar [m]')
    ax.set_xlabel('IF chirp frequency [Hz]')
#%% plot angle of returns
    fg = figure()
    ax = fg.gca()
    hi=ax.pcolormesh(xpc,ypc,angle(s))
    fg.colorbar(hi)
    ax.set_title('Angle of IF signal')
    ax.set_ylabel('x-displacement of radar [m]')
    ax.set_xlabel('IF chirp frequency [Hz]')
