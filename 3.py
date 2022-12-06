from tkinter import *
from tkinter import ttk
from tkinter.messagebox import OK, INFO, showinfo

root1 = Tk()
root1.title("Окно библиотеки!")
root1.geometry("380x150")


def click():
    showinfo(title="Окно библиотеки!",
             message="Добро пожаловать на наш сайт библиотеки!",
             detail="Привет!", icon=INFO, default=OK)


btn = ttk.Button(text="click", command=click)
btn.pack(anchor=CENTER, expand=1)

root1.mainloop()
