from tkinter import *

root = Tk()
canvas = Canvas(root, width=300, height=200)
canvas.pack()

colors = ['red', 'green', 'blue', 'yellow', 'purple']
positions = [(20,20), (80, 40), (150,60), (220,80), (100,120)]

for (x, y), c in zip(positions, colors):
    canvas.create_oval(x, y, x+40, y+40, fill=c)

root.mainloop()