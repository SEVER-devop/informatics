clc
clear

a = 0.2;       
b = 1.2;       
h = 0.1;       
y0 = 0.25;     

x = a:h:b;     
y = zeros(size(x));
y(1) = y0;     

for i = 1:length(x)-1
    y_half = y(i) + (h/2) * f3(x(i), y(i));
    y(i+1) = y(i) + h * f3(x(i) + h/2, y_half);
end

fprintf(' x\t\ty(x)\n');
fprintf('-------------\n');
for i = 1:length(x)
    fprintf('%.4f\t%.4f\n', x(i), y(i));
end

figure;
plot(x, y, '-*', 'LineWidth', 3, 'MarkerSize', 6);
title('f = 0.158 *(x^2 + sin(0.8 * x)) + 1.164 * y');
xlabel('x');
ylabel('y(x)');
grid on;
