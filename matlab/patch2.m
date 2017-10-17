%Patch antenna calculations
%based on equations from Bancroft's "Microstrip and Printed Antenna
%Design"

%Enter Er
Er = 2.6; %from board specs

%Speed of light
c = 3.0E+8; %physical constant

%frequency of interest
fr = 2.435E+9; %[Hz]


%height of board
h = 1.524E-3; %[m]

%**********************************
%calc width (radiating edge)
W = (c/(2*fr))*((Er+1)/2)^(-1/2)

%calc Er Effective
Ee=(Er+1)/2+((Er-1)/2)*((1+12*(h./W)).^(-1/2))

%calc delta 'el', change in L due to not being free space
dl = 0.412*[((Ee+0.3)*(W/h+0.264))/((Ee-0.258)*(W/h+0.8))]*h

%calc length (non-radiating edge)
L = (c/(2*fr*sqrt(Ee)))-(2*dl)