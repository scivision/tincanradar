#!/usr/bin/env python
import setuptools  # noqa: F401
from numpy.distutils.core import setup, Extension

setup(ext_modules=[Extension(name='pychirp',
                             sources=['comm.f90', 'fwdmodel.f90'])])
