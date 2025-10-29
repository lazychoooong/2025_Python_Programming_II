# frame : 가독성 향상 위해 다른 위젯을 담는 '쟁반' 역할 - 그룹화, 배치에 사용
from tkinter import *

root = Tk()
root.geometry("300x200")

frame = Frame(root, width = 200, height = 100)
frame.pack()

button1 = Button(frame, text = "버튼 1")    # 원래 frame 위치에 label 같은 거 넣었었음!
button1.pack(side = "left")

button2 = Button(frame, text = "버튼 2")
button2.pack(side = "left")

root.mainloop()

# 전체 구조 :
#  root 윈도우
#     ㄴ frame (작은 영역)
#         ㄴ button1 (왼쪽)
#         ㄴ button2 (그 옆)