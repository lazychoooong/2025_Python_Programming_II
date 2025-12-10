# 사용자가 선택한 언어(Python, Java, C++)를 Label에 표시하는 GUI를 작성하시오.
from tkinter import *

def update():
    choice = lang.get()
    if choice == 1:
        label.configure(text='선택 : Python')
    elif choice == 2:
        label.configure(text='선택 : Java')
    else:
        label.configure(text='선택 : C++')

root = Tk()
root.geometry("300x300")

lang = IntVar()

Label(root, text="Python, Java, C++ 중 선택하세요").pack()

Radiobutton(root, text='Python', variable=lang, value=1, command=update).pack(anchor=W)
Radiobutton(root, text='Java', variable=lang, value=2, command=update).pack(anchor=W)
Radiobutton(root, text='C++', variable=lang, value=3, command=update).pack(anchor=W)

label = Label(root, text="선택 : 없음")
label.pack()

root.mainloop()