a = 2;
b = 3;
n = 10;
x = linspace(a, b, n)';
y = log(tan(x / sqrt(10)));


degrees = [2, 3, 4, 5];
results = struct();

for d = degrees
    p = polyfit(x, y, d);
    y_fit = polyval(p, x);
    abs_error = abs(y - y_fit);
    rel_error = abs_error ./ abs(y);
    
    results(d).coefficients = p;
    results(d).max_abs_error = max(abs_error);
    results(d).max_rel_error = max(rel_error);
    
    fprintf('Polynomial degree %d:\n', d);
    disp('Coefficients:'); disp(p');
    fprintf('Max absolute error: %.4e\n', results(d).max_abs_error);
    fprintf('Max relative error: %.4e\n\n', results(d).max_rel_error);
end

figure;
plot(x, y, 'ko-', 'LineWidth', 1.5, 'MarkerFaceColor', 'k', 'DisplayName', 'function');
grid on;
xlabel('x');
ylabel('y');
title('y = ln(tan(x/\surd10))');
