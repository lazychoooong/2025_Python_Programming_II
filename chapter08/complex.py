from tkinter import *

root = Tk()
root.geometry("300x100")

f = Frame(root)

b1 = Button(f, text = "버튼 1", bg = "red", fg = "white")
b2 = Button(f, text = "버튼 2", bg = "green", fg = "black")
b3 = Button(f, text = "버튼 3", bg = "blue", fg = "white")

b1.pack(side = LEFT)
b2.pack(side = LEFT)
b3.pack(side = LEFT)

l = Label(root, text= "이 레이블은 버튼들 위에 배치된다.")
l.pack()
f.pack()

root.mainloop()