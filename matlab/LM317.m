%LM317 resistor calculator

%Enter R1 (Program resistor, between Vout and Adj)
R1=330

%Enter Iadj (typical 100E-6 A)
Ia=100E-6

%Enter desired Vout
Vo=8
Vo1=24

%Calculate Rs (Output Set Resistor, between Adj and Gnd)

Rs=(Vo-1.25)/((1.25/R1)+Ia)
Rs1=(Vo1-1.25)/((1.25/R1)+Ia)

%plot Vo for varying Rs "oy, what do we have in stock?"

Rs=0.9*Rs:1.1*Rs;
Vo=1.25*(1+Rs/R1)+Ia*Rs;

Rs1=0.9*Rs1:1.1*Rs1;
Vo1=1.25*(1+Rs1/R1)+Ia*Rs1;
%% plot
figure
plot(Rs,Vo);
xlabel('Rs');
ylabel('Vo');
title('Rs vs. Vo');
grid on;

figure
plot(Rs1,Vo1);
xlabel('Rs');
ylabel('Vo');
title('Rs vs. Vo');
grid on;