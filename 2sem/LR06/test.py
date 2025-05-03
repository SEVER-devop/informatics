import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def plot_graph(obj) -> None:
    try:
        # Получаем границы интервала (если не вариант 3)
        if obj.name != "Third":
            obj.left_border = float(obj.widgets[0].get())
            obj.right_border = float(obj.widgets[1].get())
    except Exception as e:
        return error(e)
    
    # Создаем фигуру с двумя subplots
    fig = Figure(figsize=(8, 6), facecolor='peachpuff')
    ax1 = fig.add_subplot(211, facecolor='bisque')  # График для y1
    ax2 = fig.add_subplot(212, facecolor='bisque')  # График для y2
    
    # Если вариант 3 (система уравнений)
    if obj.name == "Third":
        # Данные для точного решения
        x_exact = np.linspace(0, 1, 100)
        y1_exact = 2*np.exp(3*x_exact) - 4*np.exp(-3*x_exact)
        y2_exact = np.exp(3*x_exact) + np.exp(-3*x_exact)
        
        # Данные численных методов (предполагаем, что они сохранены в obj.values)
        x_num = obj.values[0]
        y1_euler, y2_euler = obj.values[1], obj.values[2]
        y1_rk, y2_rk = obj.values[3], obj.values[4]
        
        # Графики для y1(x)
        ax1.plot(x_exact, y1_exact, 'k-', label='Точное решение')
        ax1.plot(x_num, y1_euler, 'b--o', markersize=4, label='Метод Эйлера')
        ax1.plot(x_num, y1_rk, 'g--s', markersize=4, label='Рунге-Кутта 4')
        ax1.set_title('Решение y₁(x)')
        ax1.legend()
        ax1.grid(True)
        
        # Графики для y2(x)
        ax2.plot(x_exact, y2_exact, 'k-', label='Точное решение')
        ax2.plot(x_num, y2_euler, 'b--o', markersize=4, label='Метод Эйлера')
        ax2.plot(x_num, y2_rk, 'g--s', markersize=4, label='Рунге-Кутта 4')
        ax2.set_title('Решение y₂(x)')
        ax2.legend()
        ax2.grid(True)
        
    else:
        # Для обычных функций (не система)
        x = np.linspace(obj.left_border, obj.right_border, 1000)
        y = eval(obj.fun)
        ax1.plot(x, y, color='r', linestyle='solid', linewidth=2)
        ax1.set_title(f'График функции {obj.fun}')
        ax2.axis('off')  # Скрываем второй subplot
    
    # Общие настройки
    for ax in [ax1, ax2]:
        ax.axhline(y=0, color='gray', linestyle='-', linewidth=1)
        ax.axvline(x=0, color='gray', linestyle='-', linewidth=1)
    
    fig.tight_layout()
    fig.patch.set_edgecolor('whitesmoke')
    fig.patch.set_linewidth(2)
    
    # Отображаем в интерфейсе
    canvas = FigureCanvasTkAgg(fig, master=obj.win_frame)
    canvas.draw()
    canvas.get_tk_widget().place(x=10, y=300, width=800, height=600)
    obj.widgets.append(canvas)