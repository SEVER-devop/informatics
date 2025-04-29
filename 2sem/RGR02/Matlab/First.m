clc
clear
e = 0.0001;
max_iter = 100;

x = linspace(-3, 3, 1000);

figure;
plot(x, f(x), 'b-', 'LineWidth', 3);
grid on;
hold on;
plot(x, zeros(size(x)), 'k--');
title('x^3 - 3x^2 + 3 = 0');
xlabel('x');
ylabel('y');

a = input('Left border ');
b = input('Right border ');


if f(a)*ddf(a) > 0
    x = a;         
    x_t = b;   
elseif f(b)*ddf(b) > 0
    x = b;       
    x_t = a;  
else
    disp('No roots')
end

for i = 1:max_iter
    x_next = x - f(x)/df(x);
    x_t_next = x - (f(x)*(x_t - x)) / (f(x_t) - f(x));

    if abs(x_next - x_t_next) < e
        root = (x_next + x_t_next) / 2;
        disp('Root')
        disp(root)
        break;
    end

    x = x_next;
    x_t = x_t_next;
end
