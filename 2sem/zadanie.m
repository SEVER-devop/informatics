clc
figure;
hold on;
ezplot('sin(x-y) - x*y + 1', [-5 5 -5 5]);
ezplot('x^2 - y^2 - 0.75', [-5 5 -5 5]);
title('Графики обоих уравнений');
xlabel('x'); ylabel('y');
legend('sin(x-y) - xy = -1', 'x^2 - y^2 = 0.75');
grid on;
hold off;

fsolve(@functions, [1 1])
fsolve(@functions, [-1 -1])
