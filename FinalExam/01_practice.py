# 버튼을 누르면 Label의 텍스트 전환되도록 하기

from tkinter import *

def change_text():
    label.configure(text="버튼 클릭됨!")

root = Tk()
root.geometry("300x200")

label = Label(root, text="Hello Tkinter!")
label.pack()

button = Button(root, text="눌러보세요", command="change_text")
button.pack()

root.mainloop()