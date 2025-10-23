from tkinter import *
from math import *

def calculate(event):
    label.configure(text = "결과 :" + str(eval(entry.get())))

root = Tk()

Label(root, text = "파이썬 수식 입력 : ").pack()

entry = Entry(root)

entry.bind("<Return>", calculate)
entry.pack()

label = Label(root, text = "결과")
label.pack()

root.mainloop()