from tkinter import *

root = Tk()

canvas = Canvas(root, width=300, height=200)
canvas.pack()
canvas.create_polygon(10, 10, 150, 110, 250, 20, fill="blue")

root.mainloop()