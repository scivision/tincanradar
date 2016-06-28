%Patch antenna calculations
%based on equations from Bancroft's "Microstrip and Printed Antenna
%Design" ISBN 1-884932-45-2,
%Garg et al "Microstrip Antenna Design Handbook" ISBN 0-89006-513-6,
%and also Balanis' "Antenna Theory" ISBN 0-471-59268-4
%Tested with Matlab R2006a (7.2.0.232)


%Enter Er (DK)
Er = 4.0; %from board specs

%Speed of light
c = 3.0E+8; %physical constant [m/s]

%maximum desired frequency (to find maximum laminate thickness)
fmax = .915E+9 %[Hz]


%**********************************
%NOTE: Values are output in Matlab Command Window


%Bancroft AND Garg et al state h must be less than or equal to this value for patch antennas to avoid
%surface waves.  Below this height, surface wave losses (which cause end-firing etc.) "can be neglected" 
h = ((0.3*c)/(2*pi*fmax*sqrt(Er))) %[m]

%However, for patch antennas, Balanis allows for up to 1/20 wavelength, and down to 0.003
%wavelength thickness (free space wavelength).  
lambda=c/fmax %free space wavelength [m]
h003 = 0.003*lambda %0.003 free space wavelength (minimum thickness) [m]
h05 = 0.05*lambda %0.05 free space wavelength (maximum thickness) [m]

%****************
%More detailed look according to Garg et al.

%finds h for which all modes except TM0 are below cutoff--but this height is so thick that surface waves still can
%be readily created--don't pick height with this result

hcut = (1/(4*sqrt(Er-1)))*lambda % [m]

