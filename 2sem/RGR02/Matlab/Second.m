clc
clear
a = 0.8;   
b = 2.96;  

x = linspace(a, b, 100);
figure;
plot(x, f2(x), 'b-', 'LineWidth', 2);
title('График подынтегральной функции');
xlabel('x');
ylabel('y');
grid on;

% n1 = 9
n1 = 9;
h1 = (b - a)/n1;
sum1 = f2(a) + f2(b);

for i = 1:n1-1
    x = a + i*h1;
    if mod(i,3) == 0
        sum1 = sum1 + 2*f2(x);
    else
        sum1 = sum1 + 3*f2(x);
    end
end
integral1 = 3*h1/8 * sum1;

% n2 = 12
n2 = 12;
h2 = (b - a)/n2;
sum2 = f2(a) + f2(b);

for i = 1:n2-1
    x = a + i*h2;
    if mod(i,3) == 0
        sum2 = sum2 + 2*f2(x);
    else
        sum2 = sum2 + 3*f2(x);
    end
end
integral2 = 3*h2/8 * sum2;

% Tochnost
tochnost = abs(integral2 - integral1);

disp('Значение интеграла при n=9')
disp(integral1)
disp('Значение интеграла при n=12')
disp(integral2)
disp('Оценка погрешности:')
disp(tochnost)
