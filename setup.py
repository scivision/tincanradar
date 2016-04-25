#!/usr/bin/env python3
from setuptools import setup #enables develop
import subprocess

try:
    subprocess.run(['conda','install','--yes','--file','requirements.txt']) #don't use os.environ
except Exception as e:
    print('you will need to install packages in requirements.txt  {}'.format(e))

with open('README.rst','r') as f:
	  long_description = f.read()

#%%
from numpy.distutils.core import setup,Extension

#%% install
setup(name='tincanradar',
      version='0.1',
	  description='Model and Build a $35 radar from coffee cans and MMICs',
	  long_description=long_description,
	  author='Michael Hirsch',
	  url='https://github.com/scivision/tincanradar',
      packages=['tincanradar'],
      ext_modules=[Extension(name='pychirp',
                    sources=['comm.f90','fwdmodel.f90'],
                    f2py_options=['--quiet'])]
	  )


