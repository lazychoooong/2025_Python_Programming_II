from tkinter import *

root = Tk()

w = Canvas(root, width=300, height=200) # (1)
w.pack()

w.create_line(0, 0, 300, 200)       # (2)   
w.create_line(0, 0, 300, 100, fill="red")   # (3)
w.create_rectangle(50, 25, 200, 100, fill="blue")   # (4)

root.mainloop()