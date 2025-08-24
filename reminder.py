import pygame
from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import datetime
import time
t = 0
music = False
def set():
    global t
    rem = sd.askstring("Время напомнинания"
                       , "Введите время напоминания в формате ЧЧ:ММ(в 24 часовом формате )",)

    label.config(text=(f"Напоминание установлено на: {rem}"))


    if rem:
        try:
            hour = int(rem.split(":")[0])
            minute = int(rem.split(":")[1])
            now = datetime.datetime.now()
            print(now)
            dt = now.replace(hour=hour, minute=minute, second=0)
            print(dt)

            t = dt.timestamp()
            print(t)
            
            
            
        except Exception as e:
            mb.showerror("Ошибка", f"Ошибка: {e}")
            
def check():
    global t
    if t:
        now = time.time()
        if now >= t:
            play_snd()
            t = 0

    window.after(10000, check)


def play_snd():
    global music
    music = True
    pygame.mixer.init()
    pygame.mixer.music.load("1.mp3")
    pygame.mixer.music.play()
def stop():
    global music
    if music:
        pygame.mixer.music.stop()
        music = False
    label.config(text="Новое напоминание")    

window = Tk()
window.title("Reminder")
window.geometry("300x200+200+200")

label = Label(window, text="Enter your reminder", font=("Arial", 20))
label.pack(pady=10)

set_button = Button(window, text="Set Reminder", command= set)
set_button.pack(pady=10)
stop_button = Button(window, text="Stop Music", command= stop)
stop_button .pack(pady=10)  

stop_programm = Button(window, text="Stop Programm", background="red",  command= window.destroy)
stop_programm.pack(pady=10)

check()


window.mainloop()
