clc
clear
y0 = [-2; 2];       
interval = [0 1];

[x, y] = ode45(@fun2, interval, y0);

y1_tochn = 2*exp(3*x) - 4 .* exp(-3*x);
y2_tochn = exp(3*x) + exp(-3*x);

figure;
plot(x, y(:,1), 'g-', 'LineWidth', 3); 
hold on;
plot(x, y1_tochn, 'r--', 'LineWidth', 2); 
xlabel('x', 'FontSize', 12);
ylabel('y_1(x)', 'FontSize', 12);
legend('ode45', 'Точное');
title('вариант 3, y1(x)', 'FontSize', 14);
grid on;

figure;
plot(x, y(:,2), 'b-', 'LineWidth', 3);
hold on;
plot(x, y2_tochn, 'r--', 'LineWidth', 2);  
xlabel('x', 'FontSize', 12);
ylabel('y_2(x)', 'FontSize', 12);
legend('ode45', 'Точное');
title('вариант 3, y2(x)', 'FontSize', 14);
grid on;