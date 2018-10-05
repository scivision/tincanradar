%Op Amp Filter Calculator  (Sallen-Key Butterworth 4th order)

%Capacitance audit range
%(This works if you put a singular value here, e.g. 4.7E-9--will plot a
%single point)
C1=1.0E-8
C1a=4.7E-9

%Enter Butterworth Coefficients here
a1=1.8478;
a2=0.7654;

b1=1.0000;
b2=1.0000;


%calculate R1
C2=C1*((4*b1)/a1^2)

R1=(a1*C2-(sqrt((a1*C2)^2-4*b1*C1*C2)))/(4*pi*6E+4*C1*C2)
R2=(a1*C2+(sqrt((a1*C2)^2-4*b1*C1*C2)))/(4*pi*6E+4*C1*C2)

C2a=4.7E-9
%C2a=C1a*((4*b2)/a2^2)

R1a=(a2*C2a-(sqrt((a2*C2a)^2-4*b2*C1a*C2a)))/(4*pi*6E+4*C1a*C2a)
R2a=(a2*C2a+(sqrt((a2*C2a)^2-4*b2*C1a*C2a)))/(4*pi*6E+4*C1a*C2a)

assert(isreal(R1a) && isreal(R2a),'resistors cannot be complex')

figure
plot(C1,R1)
axis([1.0E-9 1.0E-8 10 10000])
xlabel('C1 Capacitance')
ylabel('R1 Value')
title('R1 vs. C1')
grid('on')

