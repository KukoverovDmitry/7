from tkinter import *
from tkinter import messagebox as mb
import random

window = Tk()
window.title("Игра угадай число")

m1 = Label(window, text="Угадай число от 1 до 100")
m1.pack()


def check():
     s = e.get()
     rnd  = random.randint(1, 2)
     if s == rnd:
          mb.showinfo(title="Угадал", message="Вы угадали")
     else:
         mb.showinfo(title="Не угадал", message="Вы не угадали", icon="warning")
    
     answer = mb.askretrycancel(title="Вопрос", message="Еще раз?")         
 
     if answer:
        e.delete(0, END)
     else:
        window.destroy()

e = Entry(window)
e.pack()


b = Button(window, text="Передать", command=check)
b.pack()

m = Label(window,height=3, width=100    )
m.pack()


window.mainloop()