from tkinter import *

def click(key):
    print("버튼 클릭:", key)

root = Tk()
root.title("계산기 버튼 테스트")

buttons = [
'7',  '8',  '9',  '+',  'C',
'4',  '5',  '6',  '-',  '  ',
'1',  '2',  '3',  '*',  '  ',
'0',  '.',  '=',  '/',  '   ' ]

# 반복문으로 버튼을 생성한다.
i = 0
for b in buttons:
    cmd = lambda x=b: click(x)                  # 클릭 시 click(x) 실행
    button = Button(root, text=b, width=5, relief='ridge', command=cmd)
    button.grid(row=i//5+1, column=i%5)         # 행/열 위치에 배치
    i += 1

root.mainloop()