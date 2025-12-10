from tkinter import *
from random import randint

def move_button():
    x = randint(0, 300)
    y = randint(0, 300)
    target.place(x=x, y=y)

root = Tk()
root.geometry("300x300")

target = Button(root, text="타겟")
target.place(x=50, y=50)

Button(root, text="Press me", command=move_button).pack()

root.mainloop()


