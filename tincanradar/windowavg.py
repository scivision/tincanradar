#!/usr/bin/env python
from numpy import cumsum,empty_like,log10,arange,nan
from numpy.random import standard_normal
from scipy.signal import savgol_filter
from matplotlib.pyplot import figure,show,draw,pause
'''
http://stackoverflow.com/questions/18517722/weighted-moving-average-in-python
'''
def moving_average(a, n=3):
    '''
    http://stackoverflow.com/questions/14313510/moving-average-function-on-numpy-scipy
    '''
    ret = cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n

def cummoving_avg(a):
    cumavg = empty_like(a)
    #warmup
    cumavg[0] = a[0]
    for i in range(a.size-1):
        cumavg[i+1] = (a[i+1] + i*cumavg[i]) / (i+1)
    return cumavg

def weightmov_avg(p,n=10):
    wavg = empty_like(p)
    wavg[:n-1] = p[:n-1]

    trinum = n*(n+1)/2
    for m in range(p.size-n):
        m += n-1
        cnum = (n*p[m] + (n-1)*p[m-1] + (n-2)*p[m-2] + (n-3)*p[m-3] +
               (n-4)*p[m-4] + (n-5)*p[m-5] + (n-6)*p[m-6] + (n-7)*p[m-7] +
               (n-8)*p[m-8] + (n-9)*p[m-9])
        ntot = p[m-n-1:m+2].sum() -p[m-n-1]
        nnum = cnum + n*p[m+1] - ntot
        wavg[m+1] = nnum/trinum
    return wavg

def sgmov(p,n=21,o=2,x=None):
    sgsig = nan*empty_like(p)
    sgsig[:n] = p[:n]

    if x is not None:
        ax = figure().gca()
        hp, = ax.plot(x,sgsig)

    #set_trace()
    for i in range(p.size-n):
        sgsig[:i+n] = savgol_filter(p[:i+n],n,o,mode='nearest')
        if x is not None:
            hp.set_ydata(sgsig)
            ax.set_xlim((x[0],x[-1]))
            draw(); pause(0.02)
    return sgsig

def noisydatagen(truesig,sigma=5):
    '''
    http://gtec.des.udc.es/web/images/pdfConferences/2008/iswcs_rodas_gonzalez_2008.pdf
    '''
    return truesig + sigma*standard_normal(truesig.shape)

if __name__ == '__main__':
    doplot = True
    x = arange(50,1,-0.05)
    sigma = 5 #[dB]

    truesig = -10-(20*log10(x) + 20*log10(2450) -27.55)
    sig = noisydatagen(truesig,sigma)
    #filtsig = moving_average(sig,10)

   # cumavg = cummoving_avg(sig)
    nw = 0
   # wavg = weightmov_avg(sig,nw)

    sgsig = sgmov(sig, 21, 2)

    if False:
        ax = figure(1).gca()
        ax.plot(truesig,color='black',label='true')
        ax.plot(sig,color='red',label='noisy')
        #ax.plot(filtsig,color='blue',label='filtered')
        ax.legend(loc='best')
        ax.set_title('moving average a posteriori (not real time)')
        ax.set_ylabel('amplitude')
        ax.set_xlabel('sample index')

    if doplot:
        ax = figure(2).gca()
        ax.plot(x[nw+2:],truesig[nw+2:],color='black',label='true')
        ax.plot(x[nw+2:],sig[nw+2:],color='red',label='noisy')
        #ax.plot(x,cumavg,color='blue',label='cumavg')
        #ax.plot(x[nw+2:],wavg[nw+2:],color='blue',linewidth=2,label='weighted avg')
        ax.plot(x[nw+2:],sgsig[nw+2:],color='blue',linewidth=3,label='smoothing')
        ax.invert_xaxis()
        ax.legend(loc='best')
        ax.set_ylabel('amplitude')
        ax.set_xlabel('distance')
        ax.grid(True)
        show()