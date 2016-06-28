% Microstrip transmission line calculator
% based on equations from Pozar's "Microwave Engineering"
%
% Matlab routine composed by Michael Hirsch based on the work
% of Gregory L. Charvat, The Electromagnetics Research Group,
% Michigan State University ( Aug. 2006).

%% DATA ENTRY
%Enter Board Parameters Here
h = 1.45E-3; %[m] height (thickness) of board
Er = 4.1; %relative dielectric constant of board (from manufacturer specs)

% Note:  Watch W/h--if it becomes less than one, uncomment the figures at
% the end of this Matlab file and use their data.
%%CALCULATIONS
% calculates effective epsilon and characteristic impedance

%% case W/H<1
Wn=.5:20; % Arbitrary boundary values
Wn=Wn.*0.1E-3;
Ereffn=(Er+1)/2+((Er-1)/2)*((1+12*(h./Wn)).^(-1/2)+0.04*(1-(Wn./h)).^2);
Zon=(60./sqrt(Ereffn)).*log(8*(h./Wn)+0.25.*(Wn./h)); %characteristic impedance of line

%calculate wavelength vs. Er.effective (scalar)
Len=1./sqrt(Ereffn); %scalar for wavelength inside strip

%% case W/H>=1
Ww=1:60; % Arbitrary boundary values
Ww=Ww.*0.1E-3;
Ereffw=(Er+1)/2+((Er-1)./(2*sqrt(1+12*h./Ww)));
Zow=120*pi./(sqrt(Ereffw).*(Ww/h+1.393+(2/3)*log(Ww/h+1.444))); %characteristic impedance of line

%calculate wavelength vs. Er.effective (scalar)
Lew=1./sqrt(Ereffw); %scalar for wavelength inside strip
%% DISPLAY

%{
%case W/H>=1

figure
plot(Ww,Zow); %Taking into account Er.effective, what must width be?
xlabel('Width of Strip Line [m]');
ylabel('Characteristic Impedance of Strip Line');
title('Width vs. Zo FOR W/H >=1');
grid on;


figure
plot(Ereffw,Zow);
xlabel('Effective Epsilon of Strip Line');
ylabel('Characteristic Impedance of Strip Line ');
title('Er.effective vs. Zo FOR W/H >=1');
grid on;

figure
plot(Ereffw,Lew);
xlabel('Er.effective');
ylabel('wavelength.strip');
title('Er.effective vs. Wavelength in strip W/H >=1');
grid on;
%}

%case W/H<1
figure
plot(Wn,Zon); %Taking into account Er.effective, what must width be?
xlabel('Width of Strip Line [m]');
ylabel('Characteristic Impedance of Strip Line');
title('Width vs. Zo FOR W/H <1');
grid on;

figure
plot(Ereffn,Zon);
xlabel('Effective Epsilon of Strip Line ');
ylabel('Characteristic Impedance of Strip Line ');
title('Ee vs. Zo W/H <1');
grid on;

figure
plot(Ereffn,Len);
xlabel('Epilson.effective');
ylabel('wavelength.strip');
title('Epsilon.effective vs. Wavelength in strip W/H <1');
grid on;

