from tkinter import *
from tkinter import ttk


def click():
    window = Tk()
    window.title("Новое окно")
    window.geometry("222x222")
    close_button = ttk.Button(window, text= "Закрыть окно", command=lambda: window.destroy())
    close_button.pack(anchor=CENTER, expand=1)


root1 = Tk()
root1.title("Окно библиотеки!")
root1.geometry("380x150")

btn = ttk.Button(text="Создать окно", command=click)
btn.pack(anchor=CENTER, expand=1)

root1.mainloop()
