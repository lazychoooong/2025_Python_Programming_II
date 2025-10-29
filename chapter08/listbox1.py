# 사용자가 선택할 수 있는 항목들을 보여주는 listbox
from tkinter import *

root = Tk()
lb = Listbox(root, height = 4)  # 4개의 항목만 보이도록 설정 -> 4칸짜리 리스트 표시
lb.pack()
lb.insert(END, "Python")    # END : 텍스트의 끝
lb.insert(END, "C")         # insert : 리스트박스에 새로운 항목 추가
lb.insert(END, "Java")
lb.insert(END, "Swift")

root.mainloop()