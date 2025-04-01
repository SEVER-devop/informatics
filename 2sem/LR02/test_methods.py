# import numpy as np
# from math import sin, cos

# # Определяем систему уравнений
# def f1(x, y):
#     return sin(x - y) - x*y + 1

# def f2(x, y):
#     return x**2 - y**2 - 0.75

# # Якобиан для метода Ньютона
# def jacobian(x, y):
#     df1_dx = cos(x - y) - y
#     df1_dy = -cos(x - y) - x
#     df2_dx = 2*x
#     df2_dy = -2*y
#     return np.array([[df1_dx, df1_dy], [df2_dx, df2_dy]])

# # Модифицированный метод простых итераций для поиска разных корней
# def simple_iteration_method(initial_guess, e=1e-3, max_iter=1000):
#     x, y = initial_guess
    
#     for _ in range(max_iter):
#         x_old, y_old = x, y
        
#         # Разные итерационные формулы для разных областей
#         if x_old >= 0:
#             x = np.sqrt(y_old**2 + 0.75)
#         else:
#             x = -np.sqrt(y_old**2 + 0.75)
            
#         y = (sin(x_old - y_old) + 1)/x_old if x_old != 0 else y_old
        
#         if abs(x - x_old) < e and abs(y - y_old) < e:
#             break
    
#     return x, y

# # Модифицированный метод Гаусса-Зейделя для поиска разных корней
# def gauss_seidel_method(initial_guess, e=1e-3, max_iter=1000):
#     x, y = initial_guess
    
#     for _ in range(max_iter):
#         x_old, y_old = x, y
        
#         # Разные формулы для разных областей
#         if x >= 0:
#             x = np.sqrt(y**2 + 0.75)
#         else:
#             x = -np.sqrt(y**2 + 0.75)
            
#         y = (sin(x - y_old) + 1)/x if x != 0 else y_old
        
#         if abs(x - x_old) < e and abs(y - y_old) < e:
#             break
    
#     return x, y

# # Метод Ньютона для поиска любого корня
# def newton_method(initial_guess, e=1e-3, max_iter=100):
#     x, y = initial_guess
    
#     for _ in range(max_iter):
#         F = np.array([f1(x, y), f2(x, y)])
#         J = jacobian(x, y)
        
#         try:
#             delta = np.linalg.solve(J, -F)
#         except np.linalg.LinAlgError:
#             break
            
#         x += delta[0]
#         y += delta[1]
        
#         if np.linalg.norm(delta) < e:
#             break
    
#     return x, y

# # Вычисление и вывод результатов
# def print_results(method, x, y):
#     print(f"{method}:")
#     print(f"x = {x:.5f}, y = {y:.5f}")
#     print(f"Проверка: f1(x,y) = {f1(x, y):.5f}, f2(x,y) = {f2(x, y):.5f}")
#     print()

# # Основная программа
# if __name__ == "__main__":
#     print("Поиск первого корня (x ≈ 1.0):")
#     # Первый корень (x > 0)
#     initial_guess1 = (1.0, 0.5)
    
#     x_si1, y_si1 = simple_iteration_method(initial_guess1)
#     print_results("Метод простых итераций (корень 1)", x_si1, y_si1)
    
#     x_gs1, y_gs1 = gauss_seidel_method(initial_guess1)
#     print_results("Метод Гаусса-Зейделя (корень 1)", x_gs1, y_gs1)
    
#     x_n1, y_n1 = newton_method(initial_guess1)
#     print_results("Метод Ньютона (корень 1)", x_n1, y_n1)
    
#     print("\nПоиск второго корня (x ≈ -1.0):")
#     # Второй корень (x < 0)
#     initial_guess2 = (-1.0, 0.5)
    
#     x_si2, y_si2 = simple_iteration_method(initial_guess2)
#     print_results("Метод простых итераций (корень 2)", x_si2, y_si2)
    
#     x_gs2, y_gs2 = gauss_seidel_method(initial_guess2)
#     print_results("Метод Гаусса-Зейделя (корень 2)", x_gs2, y_gs2)
    
#     x_n2, y_n2 = newton_method(initial_guess2)
#     print_results("Метод Ньютона (корень 2)", x_n2, y_n2)







from sympy import symbols, sin, cos, Eq, nsolve, solve, sqrt

x, y = symbols('x y')

eq1 = Eq(sin(x - y) - x*y, -1)
eq2 = Eq(x**2 - y**2, 0.75)


sol1 = nsolve([eq1, eq2], [x, y], [1.0, 0.5])
print(f"Корень 1: x = {sol1[0]}, y = {sol1[1].evalf(5)}")

sol2 = nsolve([eq1, eq2], [x, y], [-1.0, 0.3])
print(f"Корень 2: x = {sol2[0].evalf(5)}, y = {sol2[1].evalf(5)}")