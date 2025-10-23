from tkinter import *

def callback():
    """
    콜백 함수 : 버튼이 클릭되면 호출되어 버튼의 텍스트를 변경한다.
    """
    button["text"] = "버튼이 클릭되었음!"

root = Tk()

button = Button(root, text = "클릭", command = callback)
button.pack(side = LEFT)

root.mainloop()