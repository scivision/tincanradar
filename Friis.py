#!/usr/bin/env python
from tincanradar.fwdmodel import friis

from argparse import ArgumentParser
p = ArgumentParser()
p.add_argument('freq_Hz',help='frequency [Hz]',type=float)
p.add_argument('dist_m',help='distance (one-way) [meters]',type=float)
p = p.parse_args()

print(f'{friis(p.dist_m,p.freq_Hz):.2f} dB')
