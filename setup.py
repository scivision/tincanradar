#!/usr/bin/env python
install_requires=['numpy','scipy']
tests_require=['pytest','nose','coveralls']
# %%
from setuptools import find_packages
from numpy.distutils.core import setup,Extension
#%% install
setup(name='tincanradar',
      version='0.1.1',
      packages=find_packages(),
	    description='Model and Build a $35 radar from coffee cans and MMICs',
	    long_description=open('README.rst').read(),
	    author='Michael Hirsch, Ph.D.',
	    url='https://github.com/scivision/tincanradar',
      ext_modules=[Extension(name='pychirp',
                    sources=['comm.f90','fwdmodel.f90'],
                    f2py_options=['--quiet'])],
      install_requires=install_requires,
      tests_require=tests_require,
      extras_require={'plot':['matplotlib','seaborn'],
                      'tests':tests_require},
      python_requires='>=3.6',
      classifiers=[
      'Development Status :: 4 - Beta',
      'Environment :: Console',
      'Intended Audience :: Science/Research',
      'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
      'Operating System :: OS Independent',
      'Programming Language :: Python :: 3.6',
      'Programming Language :: Python :: 3.7',
      'Topic :: Scientific/Engineering',
      ],
      scripts=['CalcBeat.py','Friis.py','SAR.py','SimChirp.py',
              'FMCW_chirp_linearity.py','FS2dBm.py','ToneFinder.py'],
      include_package_data=True,
	  )


