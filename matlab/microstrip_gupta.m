%Microstrip Calculator
%based on Eq. 1.17..1.19 from Gupta's "Microstrip Lines and Slotlines" 1st
%ed.   ISBN 0-89006-074-6

%Enter Board Parameters Here
h = 1.524E-3; %[m] height (thickness) of board
Er = 4; %relative dielectric constant of board

%% CALCULATE characteristic impedance and Er.effective

%% Case W/h<2 "NARROW"

Wn=3:30; % Arbitrary boundary values--consider where W/h<2 !
Wn=Wn.*0.1E-3;
Zon=(377/(2*pi.*sqrt((Er+1)/2)))*(log((8*h)./Wn)+(1/8)*((Wn./(2.*h)).^2)-(1/2).*((Er-1)./(Er+1))*(log(pi/2)+(1./Er)*log(4/pi)));

%Er.effective for "narrow"
Ereffn=((Er+1)/2+((Er-1)/2)*((log(pi/2)+(1/Er)*log(4/pi))./log((8*h)./Wn))); %effective epsilon of line

%calculate wavelength vs. Er.effective (scalar) for case "narrow"
Len=1./sqrt(Ereffn); %scalar for wavelength inside strip

%% Case W/h>=2 "WIDE"
Ww=15:60; % Arbitrary boundary values--consider where W/h>=2 !
Ww=Ww.*0.1E-3;
Zow=(377/(sqrt(Er))*((Ww./h)+0.883+((Er+1)./(pi*Er))*(log(Ww./(2*h)+0.94)+1.451)+0.165*((Er-1)/Er.^2)).^(-1));

%Er.effective for "WIDE"
Ereffw=((Er+1)/2+((Er-1)/2)*((log(pi/2)+(1/Er)*log(4/pi))./log((8*h)./Ww))); %effective epsilon of line

%calculate wavelength vs. Er.effective (scalar) for case "WIDE"
Lew=1./sqrt(Ereffw); %scalar for wavelength inside strip
%% plot
figure
plot(Wn,Zon);
xlabel('Width of Strip Line [m]');
ylabel('Characteristic Impedance of Strip Line');
title('Width vs. Zo FOR W/H<2');
grid on;

%{
figure
plot(Ereffn,Zon);
xlabel('Er.effective');
ylabel('Characteristic Impedance of Strip Line');
title('Er.effective vs. Zo FOR W/H<2');
grid on;

figure
plot(Ereffn,Len);
xlabel('Er.effective');
ylabel('wavelength.strip');
title('Er.effective vs. Wavelength in strip FOR W/H<2');
grid on;
%}

figure
plot(Ww,Zow);
xlabel('Width of Strip Line [m]');
ylabel('Characteristic Impedance of Strip Line');
title('Width vs. Zo FOR W/H>=2');
grid on;

%{
figure
plot(Ereffw,Zow);
xlabel('Er.effective');
ylabel('Characteristic Impedance of Strip Line');
title('Er.effective vs. Zo FOR W/H>=2');
grid on;

figure
plot(Ereffw,Lew);
xlabel('Er.effective');
ylabel('wavelength.strip');
title('Er.effective vs. Wavelength in strip FOR W/H>=2');
grid on;
%}