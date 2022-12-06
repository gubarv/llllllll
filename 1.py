from tkinter import *
from tkinter import ttk


def display():
    Label["text"] = entry.get()


def clear():
    entry.delete(0, END)


root = Tk()
root.title("Окно библиотеки!")
root.geometry("380x150")


Label = ttk.Label()
Label.pack(anchor=NW, padx=8, pady=8)


entry = ttk.Entry()
entry.pack(anchor=NW, padx=8, pady=8)


entry.insert(0,"привет, студент!")


display_button = ttk.Button(text="Display", command=display)
display_button.pack(side=LEFT, anchor=N, pady=6, padx=6)

clear_button = ttk.Button(text="Clear", command=clear)
clear_button.pack(side=LEFT, anchor=N, pady=6, padx=6)


root.mainloop()