from tkinter import *

root = Tk()
Label(root, text = "선호하는 언어를 모두 선택하시오 : ").grid(row = 0, sticky = W)
# grid : 격자 배치 방식 (행(row)/열(column) 지정해 테이블처럼 배치)
# sticky : 위젯을 셀 안에서 어느 방향으로 붙일지.. (radio 예제의 anchor와 비슷)

value1 = IntVar()
Checkbutton(root, text = "Python", variable = value1).grid(row = 1, sticky = W)
value2 = IntVar()
Checkbutton(root, text = "C", variable = value2).grid(row = 2, sticky = W)
value3 = IntVar()
Checkbutton(root, text = "Java", variable = value3).grid(row = 3, sticky = W)
value4 = IntVar()
Checkbutton(root, text = "Swift", variable = value4).grid(row = 4, sticky = W)

root.mainloop()