clc

fplot(@func, [0, 1]);
title('График функции log(x + [x^2 + 8]^(1/2))');
xlabel('x');
ylabel('f(x)');
grid on;

% Анилитика
quad_result = integral(@func, 0, 1);
disp(['Аналитическое значение (quad): ', string(quad_result)]);


% Таблица
x_data = [0, 0.13, 0.26, 0.39, 0.52, 0.65, 0.79, 0.92, 1.05, 1.18, 1.31, 1.44, 1.57];
y_data = [0, 0.004, 0.033, 0.104, 0.217, 0.358, 0.5, 0.608, 0.65, 0.604, 0.467, 0.254, 0];

trapz_result = trapz(x_data, y_data);
disp(['Табличное значение (trapz):', string(trapz_result)]);


% Cимпсон
a = 0;
b = 1;
N = 27;

h = (b - a) / (N - 1);
x = linspace(a, b, N);
y = func(x);
    
    % Коэффициенты: 1 4 2 4 ... 2 4 1
coeffs = ones(1, N);
coeffs(2:2:end-1) = 4;
coeffs(3:2:end-2) = 2;
    
I = h/3 * sum(coeffs .* y);

disp(['Метод Симпсона:', string(I)])


abs_error = abs(quad_result - I);
rel_error = abs_error / quad_result * 100;

disp(['Абсолютная погрешность:', string(abs_error)]);
disp(['Относительная погрешность:', string(rel_error)]);

