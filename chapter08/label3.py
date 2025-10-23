from tkinter import *

root = Tk()
photo = PhotoImage(file = "dog2.jpeg")
label = Label(root, image = photo)
label.pack()
root.mainloop()