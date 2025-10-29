from tkinter import *
root = Tk()

canvas = Canvas(root, width=300, height=200)
canvas.pack()
canvas.create_arc(10, 10, 200, 150, extent=90, style=ARC)

root.mainloop()