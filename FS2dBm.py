#!/usr/bin/env python
from tincanradar import dbuvm2dbm

from argparse import ArgumentParser
p = ArgumentParser()
p.add_argument('dBuvm',help='dBuV/m',type=float)
p.add_argument('-d','--dist_m',help='distance (one-way) [meters]',type=float,default=3.)
p = p.parse_args()

print(dbuvm2dbm(p.dBuvm,p.dist_m))
