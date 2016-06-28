% This program Designs a filter
% Plots the impulse & step response and computes the transfer function
% For Butterworth & Chebyshev Approximations

function filters()
% Specify filter type
fprintf('\n Enter the Approximation method You will use')
type = input('\n Enter (b) for Butterworth Approximation or (c) for Chebyshev : ','s');
if (type == 'b')
    fprintf('\n You choose Butterworth Approximation : ')
    way = input('\n Enter (o) if You know the order or (d) for a filter design : ','s');
    if (way == 'd')
        wr = input('\n Enter the normalized Rejection frequency : ');
        att = input('\n Enter the Attenuation value at this frequency in dB : ');
        n = att / (20 * log10(wr));
        n = ceil(n);
        fprintf('\n The order of the filter is %d',n)
    elseif (way == 'o')
        n = input('\n Enter the order of Butterworth filter : ');
    else
        fprintf('\n Sorry! You entered a wrong choice');
    end
    % Get the poles
    for k = 1 : 2*n
        thepoles(k) = exp(j*pi*((2*k+n-1)/(2*n)));
        if (real(thepoles(k)) >= 0)
            thepoles(k) = 0;
        end
    end
    hh = find(thepoles);
    stpoles = thepoles(hh);       % Stable Poles
elseif (type == 'c')
    fprintf('\n You choose Chebyshev Approximation : ')
    way = input('\n Enter (o) if You know the order & ripple factor or (d) for a filter design : ','s');
    if (way == 'd')
        ripples = input('\n Enter the Ripples value of the passband in dB : ');
        wr = input('\n Enter the normalized Rejection frequency : ');
        att = input('\n Enter the Attenuation value at this frequency in dB : ');
        po = ripples / 10;
        const = 10 .^ po;
        eibsln = sqrt((const - 1));
        n = (att + 6 - 20 * log10(eibsln)) / (6 + 20 * log10(wr));
        n = ceil(n);
        fprintf('\n The order of the filter is %d',n)
        fprintf('\n The value of ripple factor is %d',eibsln)
    elseif (way == 'o')
        n = input('\n Enter the order of Chebyshev filter : ');
        eibsln = input('\n Enter the ripple factor of the passband : ');
    else
        fprintf('\n Sorry! You entered a wrong choice');
    end
    v = (1/n) * asinh(1/eibsln);
    siv = sinh(v);
    cov = cosh(v);
    % Get the poles
    for k = 1 : 2*n
        thepoles(k) = exp(j*pi*((2*k+n-1)/(2*n)));
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
    stpoles = restpoles + j * imstpoles;
else
    fprintf('\n Sorry! You entered a wrong choice');
end
den = poly(stpoles);
den = real(den);
H = tf(1,den)                % Transfer function
h = impulse(1,den,50);       % Impulse Response
s = step(1,den,50);          % Step Response
t = linspace(0,50,length(h));
%% plot
figure
plot(t,h)
xlabel('Time')
ylabel('Amplitude')
title('Normalized Impulse Response')
figure
plot(t,s)
xlabel('Time')
ylabel('Amplitude')
title('Normalized Step Response')
realpoles = real(stpoles);
imagpoles = imag(stpoles);
figure
plot(realpoles,imagpoles,'*')
axis([-1 1 -1.5 1.5])
grid on
xlabel('Sigma')
ylabel('j * Omega')
title('Poles of the filter in S-plane')
end