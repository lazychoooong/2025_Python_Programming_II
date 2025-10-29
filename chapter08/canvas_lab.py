
from tkinter import *
from tkinter import colorchooser

def draw_rectangle():
    fill_color = colorchooser.askcolor(title="채우기 색상 선택")[1]
    outline_color = colorchooser.askcolor(title="외곽선 색상 선택")[1]
    canvas.create_rectangle(50, 50, 200, 150, fill=fill_color, outline=outline_color)

root = Tk()

canvas = Canvas(root, width=300, height=200)
canvas.pack()

button = Button(root, text="사각형 그리기", command=draw_rectangle)
button.pack()

root.mainloop()
