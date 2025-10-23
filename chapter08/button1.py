from tkinter import *

def button_clicked():
    print("버튼이 클릭되었습니다!")

root = Tk()
root.geometry("300x200")

button = Button(root, text = "클릭하세요", command = button_clicked)
button.pack()

root.mainloop()
