% Op Amp Filter Calculator  (Sallen-Key Butterworth 4th order)
% coffee can through-wall radar prototype
% from Op Amps for Everyone (?)
% June 2006
% Michael Hirsch
% (not verified for correctness, uploaded as was)

%Enter Standard Value Capacitor here
C1 = 1.0E-6;

%Enter Butterworth Coefficients here
a1=1.8478;
a2=0.7654;

b1=1.0000;
b2=1.0000;


%calculate R1
C2=C1*((4*b1)/a1^2);

R1=(a1*C2-(sqrt((a1*C2)^2-4*b1*C1*C2)))/(4*pi*6E+4*C1*C2);
%% plot
figure
plot(C2,R1)
%axis([1.0E-9 1.0E-6 100 10000])
xlabel('C2 Capacitance')
ylabel('R1 Value')
title('R1')
grid('on')

