function z = fun3(x, y)
    z = [y(2);  % y1' = y2
            (2*exp(x) - x.^2 + y(1))];  % y2'
end