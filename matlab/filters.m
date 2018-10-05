% This program Designs a filter
% Plots the impulse & step response and computes the transfer function
% For Butterworth & Chebyshev Approximations

% works from Matlab and GNU Octave
function filters(ftype, order)

% ftype:
%   b: Butterworth
%   c: Chebyshev

if nargin < 2 
    order = []; 
else
    validateattributes(order, {'numeric'}, {'integer', 'positive', 'scalar'})    
end

validateattributes(ftype, {'char'}, {'scalar'})


try
    pkg load control
end
assert(~isempty(ver('control')), 'control toolbox required')
% Specify filter type
disp('choose filter design method:')


switch lower(ftype)
  case 'b'
        disp('Butterworth Approximation : ')
        
        if isempty(order)
            wr = input('Enter the normalized Rejection frequency : ');
            att = input('Enter the Attenuation value at this frequency in dB : ');
            order = att / (20 * log10(wr));
            order = ceil(order);
            disp(['filter order ',int2str(order)])
        end
        
        if order < 1, error('incorrect parameters'), end
        
        % Get the poles
        for k = 1 : 2*order
            thepoles(k) = exp(1j*pi*((2*k+order-1) / (2*order)));
            if (real(thepoles(k)) >= 0)
                thepoles(k) = 0;
            end
        end
        hh = find(thepoles);
        stpoles = thepoles(hh);       % Stable Poles
  case 'c'
    disp('Chebyshev Approximation :')
   
    if ~isempty(order)
        eibsln = input('ripple factor of the passband : ');
    else
        ripples = input('ripples value of the passband in dB : ');
        wr = input('normalized Rejection frequency : ');
        att = input('Attenuation value at this frequency in dB : ');
        po = ripples / 10;
        const = 10 .^ po;
        eibsln = sqrt((const - 1));
        order = (att + 6 - 20 * log10(eibsln)) / (6 + 20 * log10(wr));
        order = ceil(order);
        disp(['filter order ',int2str(order)])
        disp(['ripple factor ',int2str(eibsln)])
    end
    
    if order < 1, error('incorrect parameters'), end
    
    v = (1/order) * asinh(1/eibsln);
    siv = sinh(v);
    cov = cosh(v);
    % Get the poles
    for k = 1 : 2*order
        thepoles(k) = exp(1j*pi*((2*k+order-1) / (2*order)));
        if (real(thepoles(k)) >= 0)
            thepoles(k) = 0;
        end
    end
    hh = find(thepoles);
    stpoles = thepoles(hh);       % Stable Butterworth Poles
    % Getting Chebyshev Poles
    restpoles = real(stpoles);
    imstpoles = imag(stpoles);
    restpoles = siv * restpoles;
    imstpoles = cov * imstpoles;
    stpoles = restpoles + 1j * imstpoles;
  otherwise, error('invalid choice')
end
den = poly(stpoles);
den = real(den);
H = tf(1, den)                % Transfer function
[h, th] = impulse(H);       % Impulse Response
[s, ts] = step(H);          % Step Response
%t = linspace(0,50,length(h));
%% plot
figure
plot(th,h)
xlabel('Time')
ylabel('Amplitude')
title('Normalized Impulse Response')

figure
plot(ts,s)
xlabel('Time')
ylabel('Amplitude')
title('Normalized Step Response')

realpoles = real(stpoles);
imagpoles = imag(stpoles);
figure
plot(realpoles,imagpoles,'*')
axis([-1 1 -1.5 1.5])
grid on
xlabel('\sigma')
ylabel('j\omega')
title('Poles of the filter in S-plane')
end
