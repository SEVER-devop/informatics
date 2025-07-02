import matplotlib.pyplot as plt
import numpy as np

# Создаем массив значений x от -10 до 10 с шагом 0.1
x = np.arange(-10, 10, 0.1)

# Вычисляем значения y = x^2
y = x ** 2

# Создаем график
plt.figure(figsize=(8, 6))  # Задаем размер графика
plt.plot(x, y, label='y = x²', color='blue', linewidth=2)  # Рисуем линию
plt.title('График функции y = x²')  # Заголовок
plt.xlabel('Ось X')  # Подпись оси X
plt.ylabel('Ось Y')  # Подпись оси Y
plt.grid(True)  # Включаем сетку
plt.legend()  # Показываем легенду

# Отображаем график
plt.show()