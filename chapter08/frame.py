from tkinter import *

root = Tk()
root.geometry("300x200")

frame = Frame(root, width = 200, height = 100)
frame.pack()

button1 = Button(frame, text = "버튼 1")
button1.pack(side = "left")

button2 = Button(frame, text = "버튼 2")
button2.pack(side = "left")

root.mainloop()