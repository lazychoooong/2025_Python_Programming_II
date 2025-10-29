# 여기부터 20251002
from tkinter import *
def display_text():
    text = text_widget.get("1.0", END)  # 1.0 : 첫 번째 줄의 첫 번째 문자열 위치 / END : 텍스트 끝 위치 -> 모든 텍스트 가져오도록 설정
    print("입력된 정보 : ")
    print(text)

root = Tk()

text_widget = Text(root, width = 60, height = 10)
text_widget.pack()

button = Button(root, text = "출력", command = display_text)
button.pack()
root.mainloop()