import pygame
from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import datetime
import time

def set():
    rem = sd.askstring("Время напомнинания"
                       , "Введите время напоминания в формате ЧЧ:ММ(в 24 часовом формате )")
    if rem:
        try:
            hour = int(rem.split(":")[0])
            minute = int(rem.split(":")[1])
            now = datetime.datetime.now()
            print(now)
            dr = now.replace(hour=hour, minute=minute, second=0)
            print(dt)

            t = dt.timestamp()
            print(t)

        except Exception as e:
            mb.showerror("Ошибка", f"Ошибка: {e}")
            

window = Tk()
window.title("Reminder")

label = Label(window, text="Enter your reminder")
label.pack(pady=10)

set_button = Button(window, text="Set Reminder", command= set)
set_button.pack(pady=10)





window.mainloop()
