from tkinter import *

root = Tk()
choice = IntVar()

Label(root,
      text = "가장 선호하는 프로그래밍 언어를 선택하시오",
      justify = LEFT,
      padx = 20).pack()

Radiobutton(root, text = "Python", padx = 20, variable = choice, value = 1).pack(anchor = W)
Radiobutton(root, text = "C", padx = 20, variable = choice, value = 2).pack(anchor = W)
Radiobutton(root, text = "Java", padx = 20, variable = choice, value = 3).pack(anchor = W)
Radiobutton(root, text = "Swift", padx = 20, variable = choice, value = 4).pack(anchor = W)

root.mainloop()