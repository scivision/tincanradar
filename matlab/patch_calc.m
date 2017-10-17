%Patch antenna calculations
%based on equations from Bancroft's "Microstrip and Printed Antenna Design

%Enter Board Parameters Here
h = 1.6E-3; %[m] height (thickness) of board
Er = 4.4; %relative dielectric constant of board

%Enter maximum frequency
fmax = 2.0E+9; %[Hz]

%speed of light
c=3E+8; %[m/s]

%Output maximum height (to avoid surface waves)
h = ((0.3*c)/(2*pi*fmax*sqrt(Er)))
%%
%Approximate Ge (edge conductance)
Ge=0.00836*(W/lam0);

%Approximate Be (edge susceptance)
Be=0.01668*(dl./h)*(W./lam0)*Eeff;

%approximate effective DK
Ereff=(Er+1)/2+((Er-1)/2)*((1+12*(h./W)).^(-1/2));
%% OLD CODE below this line
%calculate effective epsilon and characteristic impedance

Zon=(60./sqrt(Ereffn)).*log(8*(h./Wn)+0.25.*(Wn./h)); %characteristic impedance of line

%calculate wavelength vs. Er.effective (scalar)
Len=1./sqrt(Ereffn); %scalar for wavelength inside strip
%% plot
figure
plot(Ww,Zow) %Taking into account Er.effective, what must width be?
xlabel('Width of Strip Line [m]')
ylabel('Characteristic Impedance of Strip Line')
title('Width vs. Zo FOR W/H >=1')
grid('on')


