from tkinter import *

root = Tk()
lb = Listbox(root, height = 4)
lb.pack()
lb.insert(END, "Python")
lb.insert(END, "C")
lb.insert(END, "Java")
lb.insert(END, "Swift")

root.mainloop()