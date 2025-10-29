from tkinter import *

root = Tk()

canvas = Canvas(root, width=400, height=200)
canvas.pack()
canvas.create_text(200, 100, text='Hello World!', fill='blue', font=('Courier', 30))

root.mainloop()