from tkinter import *

def button_clicked():
    print("버튼이 클릭되었습니다!")

root = Tk()     # 부모 위젯 생성
root.geometry("300x200")

button = Button(root, text = "클릭하세요", command = button_clicked)    # 버튼 위젯 생성, 명령을 함수로 지정
button.pack()      # 버튼 위젯 배치 (고정)

root.mainloop()     # 창 실행
