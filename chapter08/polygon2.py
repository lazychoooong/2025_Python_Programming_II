from tkinter import *

w = 300
h =200
root = Tk()

w = Canvas(root,  width=w, height=h)
w.pack()

points = [0,0, 80, 150, 250, 20]
w.create_polygon(points, outline="red", 
            fill='yellow', width=5)

root.mainloop()