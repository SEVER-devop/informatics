x_start = -1;
x_end = 4;
step = (x_end - x_start)/5;

x = x_start:step:x_end;

y = f(x);

degrees = [2, 3, 4, 5];

figure;
plot(x, y, 'o', 'DisplayName', 'Исходная функция'); 
hold on; 

for degree = degrees
    p = polyfit(x, y, degree);

    fprintf('Коэффициенты полинома степени %d: ', degree);
    fprintf('%g ', p);
    fprintf('\n');
    x_smooth = linspace(x_start, x_end, 100);
    y_poly = polyval(p, x_smooth);
    plot(x_smooth, y_poly, 'DisplayName', sprintf('Полином степени %d', degree));
end

title('Аппроксимация функции полиномами разных степеней');
xlabel('x');
ylabel('y');
legend('Location', 'best');
grid on;
hold off;