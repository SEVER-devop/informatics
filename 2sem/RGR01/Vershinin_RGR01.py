from tkinter import *
from random import randint

class Rgr01:
    def __init__(self) -> None:
        self.win = Tk()
        self.tk_widgets = []


    def __gen_rows(self) -> list:
        '''Генерирует все возможные строки без повторений'''

        letters = ['a', 'b', 'c', 'd']
        rows = []
        for i in letters:
            for j in letters:
                if j == i:
                    continue
                for k in letters:
                    if k == i or k == j: 
                        continue
                    for m in letters:
                        if m == i or m == j or m == k: 
                            continue
                        rows.append([i, j, k, m])

        return rows

    def __valid_checker(self, matrix) -> bool:
        """Проверяет уникальность букв и их количество по типам"""
        
        # Проверка столбцов
        for col in range(4):
            column = [matrix[row][col] for row in range(4)]
            if len(column) != len(set(column)):
                return False
        
        # Проверка количества букв
        letter_counts = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
        for row in matrix:
            for letter in row:
                letter_counts[letter] += 1
        
        return all(count == 4 for count in letter_counts.values())

    def find_matrix(self) -> list:
        """Находит все подходящие матрицы 4x4"""
        rows = self.__gen_rows()
        res_matrix = []
        
        # Перебираем все возможные комбинации из 4 строк
        for row1 in rows:
            for row2 in rows:
                if any(row1[col] == row2[col] for col in range(4)):
                    continue
                
                for row3 in rows:
                    if any(row1[col] == row3[col] or row2[col] == row3[col] for col in range(4)):
                        continue
                    
                    for row4 in rows:
                        if any(row1[col] == row4[col] or row2[col] == row4[col] or row3[col] == row4[col] for col in range(4)):
                            continue
                        
                        matrix = [row1, row2, row3, row4]
                        if self.__valid_checker(matrix):
                            res_matrix.append([row.copy() for row in matrix])
        
        return res_matrix


    def error(self, er='Ошибка') -> None:
        er_win = Toplevel(self.win)
        er_win.title("Ошибка")
        er_win.geometry("350x150")
        Label(er_win, text=er, font="30", bg="red").pack()

    def tkinter_fun(self) -> None:
        self.win.title("Домашняя работа №1 Вершинин АТ-24-01")
        self.win.geometry("700x400")
        self.win.attributes("-alpha", 0.96)
        self.win.config(bg="bisque")

        

        Canvas(bg="peachpuff", width=395, height=140).place(x=1, y=1)
        Label(text="Вершинин Сергей АТ-24-01\nВариант №3", font="30", bg="peachpuff").place(x=80, y=10)

        Button(self.win, text="Решить задачу", bg="bisque",font="15", command=self.disp_info).place(x=130, y=80)

        Button(self.win, text="RESET", bg="red", command=self.rst).place(x=5, y=5)

    def matrix_for_disp(self, mat) -> str:
        res = ''
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                res += str(mat[i][j]) + ' '
            res += '\n'
            
        return res

    def disp_info(self) -> None:
        self.rst()
        matrixes = self.find_matrix()
        frame_ans = Frame(master=self.win, bg="bisque")
        frame_ans.place(x=530, y=40)
        frame_examples = Frame(master=self.win, bg="bisque")
        frame_examples.place(x=220, y=180)

        Label(frame_ans, text=f"ответ\n{len(matrixes)}", font="30", bg="bisque").pack()


        Label(frame_examples, text="пример подходящей матрицы", font="30", bg="bisque").pack()
        Label(frame_examples, text=f"{self.matrix_for_disp(matrixes[randint(0, len(matrixes)-1)])} ", font="30", bg="bisque").pack()

        self.tk_widgets.extend([frame_ans, frame_examples])     


    def rst(self) -> None:
        try:
            for tk_widget in self.tk_widgets:
                tk_widget.destroy()
        except Exception as e:
            self.error(e)

    def run(self) -> None:
        self.tkinter_fun()
        self.win.mainloop()
    



app = Rgr01()

app.run()
