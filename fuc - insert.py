from tkinter import *

root = Tk()
entry = Entry(root)
entry.pack()

def add_number():
    entry.insert(END, "42")  # Добавляет "42" в конец поля
    
button = Button(root, text="Добавить", command=add_number)
button.pack()

root.mainloop()