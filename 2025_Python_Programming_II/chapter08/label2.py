from tkinter import *

root = Tk()

Label(root,
      text = "Times Font 폰트와 빨강색을 사용한다.",
      fg = "red",
      font = "Times 32 bold italic").pack()
Label(root,
      text = "Helvetica 폰트와 녹색을 사용한다.",
      fg = "blue",
      bg = "yellow",
      font = "Helvetica 32 bold italic").pack()
root.mainloop()