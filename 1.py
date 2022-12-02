from tkinter import*
from tkinter import ttk

clicks = 0
click = 0
clic = 0
def click_butt():  # функция по количеству тыков
    global clicks
    clicks += 1
    btn["text"] = f"{clicks} книг Толстого"

def click_butt2():  # функция по количеству тыков
    global click
    click += 1
    btn3["text"] = f"{click} книг Фета"

def click_butt3():  # функция по количеству тыков
    global clic
    clic += 1
    btn2["text"] = f"{clic} книг Гоголя"

root = Tk()
root.title("Окно библиотеки!")
root.geometry("380x150")

Label = Label(text="Вас приветстыует Ломоносовская библиотека! \n Чтобы нам подготовиться, укажите сколько книг хотите взять.")
Label.grid(row=1, column=1, columnspan=3, padx=10, pady=10 )

root.minsize(100,200)
root.maxsize(1000,1000)

btn = ttk.Button(text = "Толстой", command=click_butt)
btn.grid(row=2, column=1, ipadx= 6, ipady=5)

btn2 = ttk.Button(text = "Гоголь", command=click_butt3)
btn2.grid(row=2, column=2, ipadx= 5, ipady=6)

btn3 = ttk.Button(text = "Фет", command=click_butt2)
btn3.grid(row=2, column=3, ipadx= 6, ipady=5)

root.mainloop()