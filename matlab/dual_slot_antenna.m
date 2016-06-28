%Dual Slot antenna formulas
% from "Dual-Frequency Patch Antennas
% S. Maci and G. Biffi Gentili
% IEEE APS Mag, Vol 39, No 6, p. 17,  Dec 1997
% DOI: 10.1109/74.646798
% http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=646798
%
% Aug 2006
% Michael Hirsch
% not verified for correctness
%
%% user parameters
%Enter speed o' light [m/s]
c=299792458;

%Enter patch starting width [m]
W=50E-3;

%Enter starting width for slot displacment from board edge [m]
w=5E-3;

%Enter path starting length [m]
L=30E-3;
l=0.05*L; %arbitrary pg. 16 Figure 2.

%Enter board thickness [m]
t=1.5E-3;

%Enter Dielectric Constant of board
Er=4.0;

%% compute
W=0.8*W:1.2*W;
w=0.8*w:1.2*w;
% Temp patch for Ee
Ee=3.4

dW=(t/pi)*(((L/t)+0.336)/((L/t)+0.556))*[0.28+((Er+1)/Er)*[0.274+log((L/t)+2.518)]];

G=[1+((1.5*(w/W)-0.4*(l/L))/(1+(dW/W)))]^-1;

f100=c/(2*(W+dW)*sqrt(Ee)) * G;  %TODO Eqn (2) for Ee
%% plot
figure
plot(W,f100)
xlabel('Width of patch [m]')
ylabel('TM100 freq [Hz]')
title('Width of patch [m] vs. resonant freq (TM100)')
grid('on')
