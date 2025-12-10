# 사용자에게 “과목명”과 “점수”를 입력받고 버튼을 누르면 두 값을 출력하도록 프로그램을 작성하시오.
from tkinter import *

def submit():
    subject = entry_sub.get()
    score = entry_score.get()
    print("과목 :", subject)
    print("점수 :", score)

root = Tk()
root.geometry("200x200")

Label(root, text="과목명 : ").grid(row=0, column=0)
entry_sub = Entry(root)
entry_sub.grid(row=0, column=1)

Label(root, text='점수=').grid(row=1, column=0)
entry_score = Entry(root)
entry_score.grid(row=1, column=1)

Button(root, text="확인", command=submit).grid(row=2, column=0, pady=5)
Button(root, text="종료", command=root.quit).grid(row=2, column=1, pady=5)

root.mainloop()
