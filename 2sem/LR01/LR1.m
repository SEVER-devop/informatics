clc
clear

% Построение графика
x = -1:0.2:1;
y = m(x);

plot(x, y)
grid on
xlabel('x')
ylabel('F(x)')
title('График уравнения y = exp(-2*x) -2*x + 1')

% Поиск корней с помощью fsolve и fzero
f =@(x) exp(-2*x) -2*x + 1;

x01 = fzero(f, [0, 1]);
disp('X1 fzero = ')
fprintf('%.3f\n',x01)

x02 = fsolve(f, 0);
disp('X1 fsolve = ')
fprintf('%.3f\n',x02)


% Поиск корней методом дихотомии
a = input('Введите начальный интервал: ');
b = input('Введите конечный интервал: ');

e = 0.001;

if f(a) * f(b) > 0
    fprintf('На заданном интервале нет корней.\n');
else
    while (b-a)/2 > e
        c = (a + b) / 2;
        if f(c) == 0
            break;
        elseif f(c) * f(a) < 0
            b = c;
        else
            a = c;
        end
    end
    
    x03= (a + b) / 2;
    disp('X3 = ')
    fprintf('%.3f\n',x03)
end