[![image](https://travis-ci.org/scivision/tincanradar.svg?branch=master)](https://travis-ci.org/scivision/tincanradar)
[![image](https://coveralls.io/repos/github/scivision/tincanradar/badge.svg?branch=master)](https://coveralls.io/github/scivision/tincanradar?branch=master)
[![Maintainability](https://api.codeclimate.com/v1/badges/c837e410c41e163d47bd/maintainability)](https://codeclimate.com/github/scivision/tincanradar/maintainability)

# Tin Can Radar

Utilities for designing, building, and using a \$35 Tin Can Radar, from
the original 2006 prototype designed and built by Michael Hirsch and
advised by Greg Charvat.

I include utilities for designing the Wilkenson power divider used to
siphon off a sample of the transmit waveform for the homodyne receiver.

I include design equations for using coffee cans for antennas, as well
as the more broadband Linear Tapered Slot Antenna.

If you need something more, start an issue or send a message.


* FS2dBm.py       Convert field strength in dBuV/m or uV/m to 50 ohm dBm
* ToneFinder.py   Simulate noisy sinusoids from target returns
* Friis.py        Compute Free Space Path Loss (dB)

## Forward Model

A forward model of linear/non-linear FMCW chirp is provided in Python
using an optional Fortran library for speed.

## Build

-   Mac: `brew install gcc`
-   Linux: `apt install gfortran`
-   Windows: install
    [gfortran](https://www.scivision.co/install-latest-gfortran-on-ubuntu/)

### Install

    pip install -e .

### Matlab

Old scripts of some duplicity and perhaps not full correctness are in
the matlab directory.

## Optional


### Fortran

optional
```sh
cd bin
cmake ..
cmake --build .
```
