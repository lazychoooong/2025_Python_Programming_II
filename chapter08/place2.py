from tkinter import *
from random import randint

def place_random_buttons():
    for button in buttons:
        x = randint(50, 400)
        y = randint(50, 250)
        width = randint(50, 100)
        height = randint(20, 50)
        button.place(x=x, y=y, width=width, height=height)

root = Tk() #메인 윈도우 생성
root.geometry("500x300")

buttons = [] #색깔 버튼들을 저장할 리스트
colors = ["red", "green", "blue", "yellow"]

for color in colors: #colors리스트 돌면서 버튼 생성
    button = Button(root, text=color, bg=color, fg="white")
    buttons.append(button)

place_random_buttons() #버튼들을 무작위로 위치와 크기 지정

refresh_button = Button(root, text="새로고침", command=place_random_buttons)
refresh_button.place(x=150, y=250)

root.mainloop()