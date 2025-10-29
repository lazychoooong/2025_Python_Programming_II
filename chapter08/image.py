from tkinter import *

root = Tk()

canvas = Canvas(root,  width=300, height=200)
canvas.pack()

img = PhotoImage(file="chapter08/dog2.gif")
canvas.create_image(20, 20, anchor=NW, image=img)

root.mainloop()