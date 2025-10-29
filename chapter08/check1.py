from tkinter import *
from tkinter.messagebox import showinfo     # 팝업창 띄우는 함수
root = Tk()
root.geometry("300x200")
root.title("Checkbox demo")

agree = StringVar() # Tk 문자열 변수

agree.set("비동의") # 초기 상태 비동의로 설정 (체크박스 꺼진 상태)

def event_proc():
    showinfo(title = "결과", message = agree.get())

Checkbutton(root,
            text = "동의합니다",
            command = event_proc,
            variable = agree,
            onvalue = "동의",
            offvalue = "비동의").pack()

root.mainloop()