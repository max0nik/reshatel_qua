#! /usr/bin/env python
# -*- coding: utf-8 -*-
# ура. теперь и по-русски!
# import Tkinter
# tkinter._test()

#грузим модули для окошек и модуль математики

from math import sqrt
from Tkinter import *


#вспомнить математику для начальной школы - самое сложное!

def solver(a,b,c):


    D = b*b - 4*a*c
    if D >= 0:
        x1 = (-b + sqrt(D)) / (2*a)
        x2 = (-b - sqrt(D)) / (2*a)
        text = "Дискриминант равен: %s \n X1 is: %s \n X2 is: %s \n" % (D, x1, x2)
    else:
        text = "Дискриминант равен: %s \nУравнение не имеет решений" % D
    return text

def inserter(value):
#	инсертим
    output.delete("0.0","end")
    output.insert("0.0",value)

def clear(event):
    #очищаем вводную форму
    caller = event.widget
    caller.delete("0", "end")

def handler():
    #получаем значения
    try:
        # проверяем все ли в порядке со введенными значениями
        a_val = float(a.get())
        b_val = float(b.get())
        c_val = float(c.get())
        inserter(solver(a_val, b_val, c_val))
    except ValueError:
        inserter("Вы уверены что ввели три числа ?")

#главное окно!
root = Tk()
root.title("Число Пи и решатель квадратного уравнения")

#размер окошка посмотреть, как-то странно работает
root.minsize(400,400)
# пагаризантали (с)
root.resizable(width=True, height=False)

#поля для ввода

frame = Frame(root)
frame.grid()

a = Entry(frame, width=3)
a.grid(row=1,column=1,padx=(10,0))
a.bind("<FocusIn>", clear)
a_lab = Label(frame, text="x^2+").grid(row=1,column=2)

b = Entry(frame, width=3)
b.bind("<FocusIn>", clear)
b.grid(row=1,column=3)
b_lab = Label(frame, text="x+").grid(row=1, column=4)

c = Entry(frame, width=3)
c.bind("<FocusIn>", clear)
c.grid(row=1, column=5)
c_lab = Label(frame, text="= 0").grid(row=1, column=6)

#создаем кнопку-решалку

but = Button(frame, text="Решить", command=handler).grid(row=1, column=7, padx=(10,0))

output = Text(frame, bg="Green", font="Arial 25", width=35, height=10)
output.grid(row=2, columnspan=8)

#вызываем основной метод окошка

#посмотреть как убрать системные кнопки типа root.overrideredirect(1)
root.mainloop()
