import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-30, 30, 400)

a = -1
b = x - 2
c = 2*x**2 + 2*x + 6


D = b**2 - 4*a*c
y1_positive = (-b + D**(1/2)) / (2*a)
y1_negative = (-b - D**(1/2)) / (2*a)
y2 = 0.5 * x**2 + 1

plt.figure(figsize=(10, 6))
plt.plot(x, y1_positive, label='2*x^2 - x*y - y^2 + 2*x - 2*y + 6 = 0', color='blue')
plt.plot(x, y1_negative, color='blue')
plt.plot(x, y2, label='y - 0.5*x^2 - 1 = 0', color='red')

plt.title('Графики двух уравнений')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black',linewidth=0.5, ls='--')
plt.axvline(0, color='black',linewidth=0.5, ls='--')
plt.grid()
plt.legend()
plt.ylim(-10, 10)
plt.show()
