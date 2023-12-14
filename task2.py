import tkinter as tk 
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("T-Town Veterinary Clinic Database")
dogphoto = PhotoImage(file="dog.png")
dog = tk.Label(window, image=dogphoto)
button1 = tk.Button(window,text="Search by name")
search = tk.Entry(window,text="a", width=10)
title = tk.Label(window,text="Client Database")
entry1 = tk.Entry(window,text="Name", borderwidth=3, relief=SUNKEN)
entry2 = tk.Entry(window,text="Type", borderwidth=3, relief=SUNKEN)
entry3 = tk.Entry(window,text="Breed", borderwidth=3, relief=SUNKEN)
entry4 = tk.Entry(window,text="Owner", borderwidth=3, relief=SUNKEN)
entry5 = tk.Entry(window,text="Birthplace", borderwidth=3, relief=SUNKEN)
label1 = tk.Label(window,text="Name")
label2 = tk.Label(window,text="Type")
label3 = tk.Label(window,text="Breed")
label4 = tk.Label(window,text="Owner")
label5 = tk.Label(window,text="Birthplace")
Next = tk.Button(window,text = "Next >")
Back = tk.Button(window,text = "< Back")
button2 = tk.Button(window,text="Save\nEntry")

dog.grid(row = 1, column = 1, rowspan = 3)
button1.grid(row = 1, column = 4)
search.grid(row = 1, column = 5)
title.grid(row = 2, column = 3)
entry1.grid(row = 7, column = 1)
entry2.grid(row = 7, column = 2)
entry3.grid(row = 7, column = 3)
entry4.grid(row = 7, column = 4)
entry5.grid(row = 7, column = 5)
label1.grid(row = 6, column = 1)
label2.grid(row = 6, column = 2)
label3.grid(row = 6, column = 3)
label4.grid(row = 6, column = 4)
label5.grid(row = 6, column = 5)
Next.grid(row = 8, column = 5)
Back.grid(row = 8, column = 1)
button2.grid(row = 8, column = 3)

window.mainloop()