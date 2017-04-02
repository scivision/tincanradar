#!/usr/bin/env python

from tincanradar import range2beat,bw2rangeres

if __name__ == '__main__':
    from argparse import ArgumentParser
    p = ArgumentParser(description='calculate beat frequencies returned by stationary point targets via FMCW stimulus')
    p.add_argument('-r','--range',help='range(s) to point target [meters]',type=float,nargs='+',default=[1,10,50])
    p.add_argument('-tm',help='sweep time [sec]',type=float,default=0.1)
    p.add_argument('-b','--bw',help='RF bandwidth [Hz] over which you sweep e.g. 10.2 GHz - 10.7 GHz is 500e6',type=float,default=500e6)
    p = p.parse_args()

    fb = range2beat(p.range,p.tm,p.bw)

    rngres = bw2rangeres(p.bw)

    print('For point target ranges {} meters you may expect beat tones {} Hz.'.format(p.range,['{:.3f}'.format(f) for f in fb]))
    print(f'Using {p.bw/1e6} MHz RF bandwidth, you may expect {rngres:.3f} meters range resolution.')
