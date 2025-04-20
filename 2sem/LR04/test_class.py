import math

class RootFinder:
    def __init__(self):
        self.values = [None for _ in range(5)]
        self.widgets = []
        self.eps = 1e-3
        self.a = 0
        self.b = 1


    def __func(self, x) -> None:
        return math.log(x + math.sqrt(x*x + 8))


    def __left_rectangle_integral(self, precision=1e-3) -> None:
        func = self.__func
        a = self.a
        b = self.b
        n = 1
        integral_prev = 0.0
        while True:
            h = (b - a) / n
            integral = 0.0
            for i in range(n):
                x = a + i * h
                integral += func(x)
            integral *= h
            
            if n > 1 and abs(integral - integral_prev) < precision:
                break
            integral_prev = integral
            n *= 2
        self.values[0] = integral


    def __mid_rectangle_integral(self, precision=1e-3) -> None:
        func = self.__func
        a = self.a
        b = self.b
        n = 1
        n = 1
        integral_prev = 0.0
        while True:
            h = (b - a) / n
            integral = 0.0
            for i in range(n):
                x = a + (i + 0.5) * h
                integral += func(x)
            integral *= h
            
            if n > 1 and abs(integral - integral_prev) < precision:
                break
            integral_prev = integral
            n *= 2
        self.values[1] = integral


    def __right_rectangle_integral(self, precision=1e-3) -> None:
        func = self.__func
        a = self.a
        b = self.b
        n = 1
        n = 1
        integral_prev = 0.0
        while True:
            h = (b - a) / n
            integral = 0.0
            for i in range(n):
                x = a + (i + 1) * h
                integral += func(x)
            integral *= h
            
            if n > 1 and abs(integral - integral_prev) < precision:
                break
            integral_prev = integral
            n *= 2
        self.values[2] = integral


    def __trapezoidal_integral(self, precision=1e-3) -> None:
        func = self.__func
        a = self.a
        b = self.b
        n = 1
        n = 1
        integral_prev = 0.0
        while True:
            h = (b - a) / n
            integral = 0.5 * (func(a) + func(b))
            for i in range(1, n):
                x = a + i * h
                integral += func(x)
            integral *= h
            
            if n > 1 and abs(integral - integral_prev) < precision:
                break
            integral_prev = integral
            n *= 2
        self.values[3] = integral


    def __simpson_integral(self, precision=1e-3) -> None:
        func = self.__func
        a = self.a
        b = self.b
        n = 1
        n = 2  # Должно быть четным для метода Симпсона
        integral_prev = 0.0
        while True:
            h = (b - a) / n
            integral = func(a) + func(b)
            for i in range(1, n):
                x = a + i * h
                if i % 2 == 0:
                    integral += 2 * func(x)
                else:
                    integral += 4 * func(x)
            integral *= h / 3
            
            if n > 2 and abs(integral - integral_prev) < precision:
                break
            integral_prev = integral
            n *= 2
        self.values[4] = integral


    def get_roots(self):
        self.__left_rectangle_integral()
        self.__mid_rectangle_integral()
        self.__right_rectangle_integral()
        self.__trapezoidal_integral()
        self.__simpson_integral()

        return self.values


a = RootFinder()
res = a.get_roots()
print(res)