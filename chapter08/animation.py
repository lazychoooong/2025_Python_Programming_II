from tkinter import *

def move_oval():
    canvas.move(id, 3, 0)
    if canvas.coords(id)[2] < 400:
        root.after(50, move_oval)

root = Tk()

canvas = Canvas(root, width = 400, height = 300)
canvas.pack()

id = canvas.create_oval(10, 100, 50, 150, fill = "green")
move_oval()

root.mainloop()