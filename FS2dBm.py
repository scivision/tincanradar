#!/usr/bin/env python
from tincanradar import dbuvm2dbm,uvm2dbm

from argparse import ArgumentParser
p = ArgumentParser()
p.add_argument('-u','--uvm',help='uV/m',type=float)
p.add_argument('-db','--dBuvm',help='dBuV/m',type=float)
p.add_argument('-d','--dist_m',help='distance (one-way) [meters]',type=float,default=3.)
p = p.parse_args()

if p.dBuvm is not None:
    print(f'{p.dBuvm} dBuV/m  @ {p.dist_m} m => {dbuvm2dbm(p.dBuvm,p.dist_m):.2f} dBm')

if p.uvm is not None:
    print(f'{p.uvm} uV/m  @ {p.dist_m} m => {uvm2dbm(p.uvm,p.dist_m):.2f} dBm')