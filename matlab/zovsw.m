%Microstrip transmission line calculator

%Enter Board Parameters Here
h = .51E-3; %[m] height (thickness) of board
Eps = 3.2; %reletive dielectric constant of board

%calculate effectiv epsilon and characteristic impedance
W=1:100; % Arbitrary boundary values
W=W.*0.1E-3; %[m] width of u strip line, program rips through an arbitrary number of widths
Ee=(Eps+1)/2+((Eps-1)./(2*sqrt(1+12*h./W))); %effective epsilon of line
Zo=120*pi./(sqrt(Ee).*(W/h+1.393+0.667*log(W/h+1.444))); %characteristic impedance of line

figure
plot(W,Zo); %Taking into account Ereff, what must width be?
xlabel('Width of Strip Line [m]');
ylabel('Characteristic Impedance of Strip Line');
title('Width vs. Zo');
grid on;

figure
plot(Ee,Zo); 
xlabel('Effective Epsilon of Strip Line');
ylabel('Characteristic Impedance of Strip Line');
title('Ee vs. Zo');
grid on;