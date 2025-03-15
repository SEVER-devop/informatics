from tkinter import *


def work():
    mat = [[None for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            mat[i][j] = i
    
    fr1 = Frame()
    fr1.place(x=10, y=80)
    Label(fr1, text="Исходная матрица").grid(row=1, column=1, columnspan=2)
    for i in range(len(mat)):
        Label(fr1, text=mat[i]).grid(row=i+2, column=1, pady=1)
    
    error = Toplevel(win)
    error.title("Error")
    error.geometry("300x300")
    Label(error, text="Error").pack()

    data = []
    for i in range(len(mat)):
        strings = ""
        for j in mat[i]:
            strings += str(j) + " "
        strings += "\n"
        data.append(strings)


    with open("new", "w+") as f:
        f.writelines(data)



win = Tk()
win.geometry("900x500")
win.title("Vershinin")
Label(text="Вершинин").place(x=10,y=10)
Button(text='Work', command=work).place(x=10, y=40)




win.mainloop()