from tkinter import *
from math import *

def calculate(event): # event 매개변수 (이벤트 정보) 가 자동 전달
    label.configure(text = "결과 : " + str(eval(entry.get())))

root = Tk()

Label(root, text = "파이썬 수식 입력 : ").pack()

entry = Entry(root)

entry.bind("<Return>", calculate)   # return 누르면 calculate 호출
entry.pack()

label = Label(root, text = "결과")
label.pack()

root.mainloop()