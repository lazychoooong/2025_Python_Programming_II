from tkinter import *

root = Tk()
choice = IntVar() # 정수형 변수 : 사용자의 선택을 숫자로 저장 (1, 2, 3, 4)

Label(root,
      text = "가장 선호하는 프로그래밍 언어를 선택하시오",
      justify = LEFT,   # 왼쪽 정렬
      padx = 20).pack()

Radiobutton(root, text = "Python", padx = 20, variable = choice, value = 1).pack(anchor = W)
Radiobutton(root, text = "C", padx = 20, variable = choice, value = 2).pack(anchor = W)
Radiobutton(root, text = "Java", padx = 20, variable = choice, value = 3).pack(anchor = W)
Radiobutton(root, text = "Swift", padx = 20, variable = choice, value = 4).pack(anchor = W)
# variable은 모두 같아야 함 (어떤 버튼을 눌렀는지 저장할 것이기 때문)
# -> value 에서 숫자를 받아서 choice에 저장함 (정수형 변수) / anchor = W : 버튼 쌓기 왼쪽 정렬

root.mainloop()