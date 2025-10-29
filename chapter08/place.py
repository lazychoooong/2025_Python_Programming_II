from tkinter import *

root = Tk()
root.geometry("300x100")

button1 = Button(root, text="버튼 1", bg="red", fg="white")
button1.place(x=0, y=0)

button2 = Button(root, text="버튼 2", bg="green", fg="black")
button2.place(x=30, y=30)

button3 = Button(root, text="버튼 3", bg="blue", fg="white")
button3.place(x=60, y=60)

root.mainloop()