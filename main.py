from tkinter import *
from tkinter import ttk
import calculator_logic as c

oper = ""
first = 0
second = 0

def validte_entry(event):
    e = entry.get()
    txt = "".join(b for b in e if b in "0123456789.-")
    if e != txt:
        entry.delete(0, END)
        entry.insert(0, txt)


def calc():
    second = float(entry.get())
    if oper == "+":
        result = c.add(first,second)
    elif oper == "-":
        result = c.subtract(first,second)
    elif oper == "*":
        result = c.multiply(first,second)
    elif oper == "/":
        result = c.divide(first,second)
    entry.delete(0, END)
    entry.insert(0, str(result  ))


def enter_nimber(number):
    
    entry.insert(END, number)
 
   


def clear_entry():
    entry.delete(0, END)


def set_oper(operation):

    global first
    global second
    global  oper

    first = float(entry.get())
    oper = operation
    entry.delete(0, END)
    


window = Tk()
window.title("Calculator")

entry = ttk.Entry  (window, width=40)
entry.grid(row= 0, column=0, columnspan=4,sticky=EW)

entry.bind("<KeyRelease>", lambda event : validte_entry(event))







ttk.Button(window, text="1", command=lambda: enter_nimber(1)).grid(row=1, column=0      )
ttk.Button(window, text="2", command=lambda: enter_nimber(2)).grid(row=1, column=1      )   
ttk.Button(window, text="3", command=lambda: enter_nimber(3)).grid(row=1, column=2    ) 
ttk.Button(window, text="4", command=lambda: enter_nimber(4)).grid(row=2, column=0      ) 
ttk.Button(window, text="5", command=lambda: enter_nimber(5)).grid(row=2, column=1      ) 
ttk.Button(window, text="6", command=lambda: enter_nimber(6)).grid(row=2, column=2      ) 
ttk.Button(window, text="7", command=lambda: enter_nimber(7)).grid(row=3, column=0      ) 
ttk.Button(window, text="8", command=lambda: enter_nimber(8)).grid(row=3, column=1      ) 
ttk.Button(window, text="9", command=lambda: enter_nimber(9)).grid(row=3, column=2      ) 
ttk.Button(window, text="0", command=lambda: enter_nimber(0)).grid(row=4, column=0      ) 

ttk.Button(window, text="C", command= clear_entry).grid(row=4, column=1      ) 
ttk.Button(window, text="=", command= calc).grid(row=4, column=2    )

ttk.Button(window, text="+", command=lambda: set_oper("+")).grid(row=1, column=3 ) 
ttk.Button(window, text="-", command=lambda: set_oper("-")).grid(row=2, column=3 ) 
ttk.Button(window, text="*", command=lambda: set_oper("*")).grid(row=3, column=3 ) 
ttk.Button(window, text="/", command=lambda: set_oper("/")).grid(row=4, column=3 ) 

window.mainloop()



