clc
clear
interval = [0 1];
y0 = 1;  

[x, y] = ode45(@fun1, interval, y0);

y_tochn = (x + 1) .* exp(-sin(x));

figure;
plot(x, y, 'g-', 'Linewidth', 2);
hold on;
plot(x, y_tochn, 'r--', 'Linewidth', 3);
xlabel('x', 'FontSize', 12);
ylabel('y(x)', 'FontSize', 12);
legend('ode45', 'Точное');
title('вариант 3', 'FontSize', 14);
grid on;