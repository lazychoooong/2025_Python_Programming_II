from tkinter import *

def key_press(event):
    print("키가 눌렸습니다 :", event.keysym)
    # keysym : 키를 눌렀을 때의 값을 가져옴

root = Tk()
root.geometry("200x200")

root.bind("<Key>", key_press)
root.focus_set()

root.mainloop()