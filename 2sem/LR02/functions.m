function F = functions(xy)
    % Система нелинейных уравнений
    x = xy(1);
    y = xy(2);
    
    F = [sin(x - y) - x*y + 1;
         x^2 - y^2 - 0.75];
end