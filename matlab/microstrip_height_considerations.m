%Planar waveguide model of microstrip line
%based on Gupta's "Microstrip Lines and Slotlines" pg.27-28.
%ISBN 0-89006-074-6

%Enter physical height and width of microstrip (width calculated in another
%Matlab M-file)
h = 1.524E-3; %[m]
W = 3.9E-3; %[m]

%Enter DK of laminate;
Er = 3.0;

%Enter impedance of microstrip
Z = 50; %[ohms]

%speed of light (free space)
c = 3.0E+8; %[m/s]

%Enter frequency of interest
f = 25E+9; %[Hz]

%Enter cutoff mode (m,0) of interest
m = 1;

%%

%Calculate Er effective at zero frequency (quasi-static analysis)
Ee0=(Er+1)/2+((Er-1)/2)*((1+12*(h./W)).^(-1/2))

%calculate We0 (Effective width at zero frequency) NOTE: This is the
%"parallel plate" model, which acts as if there were two parallel plates of
%equal width (somewhat larger than the physical microstrip width),
%hearkening back to the two-wire transmission line origins...
We0=(120*pi*h)/(Z*sqrt(Ee0))

%calculate fg
fg=c/(2*W*sqrt(Er));

%calculate effective width at a given frequency
Wef=W+((We0-W)/(1+(f/fg)))

%% Frequency dependant Episilon calculations

%Calculate P (arbitrary term, for simplicity)
P = ((h/Z)^1.33)*(0.43*f^2-0.009*f^3);

%calculate Er effective at a given frequency
Eef = Er-((Er-Ee0)/(1+P))
%%
%calculate frequency dependant impedance
Zf = (120*pi*h)/(Wef*sqrt(Eef))

%Now, let's calculate the cutoff freqeuncy for mode (m,0)
fcm = (m*c)/(2*sqrt(Eef)*Wef)

%% Calculate guide wavelength for hybrid modes

%calculate (free space) wavelength
lambda=c/f;

%guide wavelength for hybrid modes
HEm = lambda/(sqrt(Eef)*sqrt(1-(fcm/f)^2))
