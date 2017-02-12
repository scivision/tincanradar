#!/usr/bin/env python
from setuptools import setup #enables develop

req =['nose','numpy','matplotlib','seaborn']

import pip
pip.main(['install','numpy'])

#%%
from numpy.distutils.core import setup,Extension

#%% install
setup(name='tincanradar',
      version='0.1',
	  description='Model and Build a $35 radar from coffee cans and MMICs',
	  author='Michael Hirsch, Ph.D.',
	  url='https://github.com/scivision/tincanradar',
      install_requires=req,
      packages=['tincanradar'],
      ext_modules=[Extension(name='pychirp',
                    sources=['comm.f90','fwdmodel.f90'],
                    f2py_options=['--quiet'])]
	  )


