from tkinter import *

def callback():
    """
    콜백 함수 : 버튼이 클릭되면 호출되어 버튼의 텍스트를 변경한다.
    """
    button["text"] = "버튼이 클릭되었음!"   # 버튼 글씨가 클릭 -> 버튼이 클릭되었음으로 바뀌게 함

root = Tk()

# command에 callback 함수 지정 -> 버튼 클릭할 때 함수 자동 호출됨
button = Button(root, text = "클릭", command = callback) # callback() 는 X! 프로그램 시작 시점에 바로 실행되어 버림
button.pack(side = LEFT)

root.mainloop()