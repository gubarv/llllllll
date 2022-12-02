from tkinter import*
from tkinter import ttk

clicks = 0
def click_butt():
    global clicks
    clicks += 1
    btn["text"] = f"{clicks} книг"

root = Tk()
root.title("Окно библиотеки!")
root.geometry("1000x250")

Label = Label(text="Вас приветстыует Ломоносовская библиотека! Чтобы нам подготовиться, укажите сколько книг хотите взять. (Одно нажатие равно одной книги)")
Label.pack()

root.minsize(100,200)
root.maxsize(1000,1000)

btn = ttk.Button(text="0", command=click_butt)
btn.pack()

root.mainloop()
