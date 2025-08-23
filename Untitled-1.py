from tkinter import *

from tkinter import messagebox as mb

window = Tk()

def check():
    answer = mb.askyesno(title="Вопрос", message="Вы уверены?",icon="warning")
    if answer:
        s = e.get()
        e.delete(0, END)
        m["text"] = s

e = Entry(window)
e.pack()


b = Button(window, text="Передать", command=check)
b.pack()

m = Label(window, height=3, width=30    )
m.pack()


window.mainloop()
