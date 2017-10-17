%Microstrip discontinuities
%from "Microstrip & Printed Antenna Design", Bancroft, R. ISBN 1-884932-45-2


%input height and width of ustrip (calculated by other Matlab M-file).
h = 1.6E-3; %[m]
W = 3.1E-3; %[m]
Er = 4.4; %DK of board

%inputs for tee only
Z1 = 50; %impedance of thru line
Z2 = 50; %impedance of shunt line

%****************
%The usual Er_effective approximation
Ereff=(Er+1)/2+((Er-1)/2)*((1+12*(h./W)).^(-1/2))
Erefft=Ereff; %change if thru line has different Er_effective than shunt arm

%Shortening of open circuit'd stub, due to EM fringing.
dL = 0.412*((Ereff+0.3)/(Ereff-0.258))*(((W/h)+0.262)/((W/h)-0.813))*h

%Shortening of Tee junction, due to shortened current paths
D2 = ((120*pi)/(Z1*Erefft))*(0.5-0.16*(Z1/Z2)*[1-2*log(Z1/Z2)])*h
