# from tkinter import *

# def zbroj(a,b):
#     a,b=int(a), int(b)
#     return  "Zbroj je: ", a+b
# def funkcija():
#     x=unos1.get() 
#     y=unos2.get()
#     labela.config(text=zbroj(x,y))

# root=Tk()
# root.title("Demo")

# unos1= Entry(root, width =100)
# unos1.grid(row=0, column=0)

# unos2= Entry(root, width =100)
# unos2.grid(row=0, column=1)

# tipka=Button(root, text="tipka", command=funkcija)
# tipka.grid(row=1, column=0)

# labela=Label(root, text="ovde se prikazuje tekst")
# labela.grid(row=2, column=0)


# root.mainloop()

import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN
import math

win = tk.Tk()
win.title('Calculator')

frame = tk.Frame(win, bg="skyblue", padx=10)
frame.pack()

entry = tk.Entry(frame, relief=SUNKEN, borderwidth=3, width=30)
entry.grid(row=0, column=0, columnspan=3, ipady=2, pady=2)

def click(num):
    entry.insert(tk.END, num)

def equal():
    try:
        res = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, res)
    except:
        tkinter.messagebox.showinfo("Error", "Syntax Error")

def clear():
    entry.delete(0, tk.END)

buttons = [
    ('1', 1, 0), ('2', 1, 1), ('3', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('7', 3, 0), ('8', 3, 1), ('9', 3, 2),
    ('0', 4, 1), ('+', 5, 0), ('-', 5, 1),
    ('*', 5, 2), ('/', 6, 0), ('sum',4,0)
]

for txt, r, c in buttons:
    tk.Button(frame, text=txt, padx=15, pady=5, width=3, command=lambda t=txt: click(t)).grid(row=r, column=c, pady=2)

tk.Button(frame, text="Clear", padx=15, pady=5, width=12, command=clear).grid(row=6, column=1, columnspan=2, pady=2)
tk.Button(frame, text="=", padx=15, pady=5, width=9, command=equal).grid(row=7, column=0, columnspan=3, pady=2)

win.mainloop()