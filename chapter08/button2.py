from tkinter import *

root = Tk()

button = Button(
    text = "This is a button!",
    width = 30,
    height = 10,
    bg = "blue",
    fg = "yellow"
)
# 버튼 요소 정해주기 (들어갈 글자, 가로 / 세로, 누르기 전 색깔 / 누를 때 색깔)

button.pack()
root.mainloop()