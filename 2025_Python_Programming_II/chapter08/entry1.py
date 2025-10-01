from tkinter import *

def get_entry_value():
    value = entry.get()
    print("입력된 값 :", value)

root = Tk()
root.geometry("300x200")

entry = Entry(root)
entry.pack()

button = Button(root, text = "확인", command = get_entry_value)
button.pack()

root.mainloop()