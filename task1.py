import tkinter as tk 
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("task1")
entry1 = tk.Entry(window,text="a", width=10)
x = tk.Label(window,text="x",)
entry2 = tk.Entry(window,text="b", width=10)
eq = tk.Label(window,text="=",)
answer = tk.Entry(window,text="answer", width=10)
entry1.grid(row = 1, column = 1)
x.grid(row = 1, column = 2)
entry2.grid(row = 1, column = 3)
eq.grid(row = 1, column = 4)
answer.grid(row = 1, column = 5)

window.mainloop()