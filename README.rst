=============
tin-can-radar
=============

Utilities for designing, building, and using a $35 Tin Can Radar, from the original 2006 prototype designed and built by Michael Hirsch and advised by Greg Charvat.

I include utilities for designing the Wilkenson power divider used to siphon off a sample of the transmit waveform for the homodyne receiver.

I include design equations for using coffee cans for antennas, as well as the more broadband Linear Tapered Slot Antenna.

If you need something more, start an issue or send a message.

Forward Model
=============
A forward model of linear/non-linear FMCW chirp is provided in Python using Fortran library for speed.


Install
=======
::

    python setup.py develop


Optional
========

Fortran
-------------------
::

    cd bin
    cmake ..
    make


Cmake
-----
Need a newer version of Cmake? It's `simple. <https://gist.github.com/scienceopen/15c104d825289aa2c0f3489495fb01e5>`_
