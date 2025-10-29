from tkinter import *

def get_entry_value():
    value = entry.get() # get = 메소드
    print("입력된 값 :", value) # 입력받은 값을 value에 저장

root = Tk()
root.geometry("300x200")

entry = Entry(root)
entry.pack()

# button : 객체를 가리키는 변수 / Button : 클래스 (헷갈리지 말기)
button = Button(root, text = "확인", command = get_entry_value) # 명령 함수로 지정 (윈도우에서 값 입력하면 터미널에서 출력)
button.pack()

root.mainloop()