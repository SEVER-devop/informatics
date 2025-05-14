clc
clear
y0 = [4; 1];
interval = [0 1];

[x, y] = ode45(@fun3, interval, y0);

y_tochn = (1+x) .* exp(x) + exp(-x) + x.^2 + 2;

figure;
plot(x, y(:,1), 'g-', 'Linewidth', 2);
hold on;
plot( x, y_tochn, 'r--', 'Linewidth', 3);
xlabel('x', 'FontSize', 12);
ylabel('y(x)', 'FontSize', 12);
legend('ode45', 'Точное');
title('вариант 3', 'FontSize', 14);
grid on;