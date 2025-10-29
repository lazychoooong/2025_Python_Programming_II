'''
문제 4. 라디오버튼을 이용한 도형 그리기 
(※ 아래 그림 예시는 예시일 뿐, 위치와 색상은 동일하지 않아도 됨.)

1. 윈도우의 제목은 “중간고사 4번” 으로 한다.
2. 윈도우 크기는 400×400으로 한다.
3. 흰색 배경의 Canvas를 하나 만든다.
4. 라디오 버튼(Radiobutton) 을 이용하여 사용자가 사각형, 원, 텍스트 중 하나를 선택할 수 있도록 한다.
- 사각형 선택 시 → 빨간 사각형(red)
- 원 선택 시 → 파란색 원(blue)
- 텍스트 선택 시 → "Hello Tkinter" (파란색 글씨, 폰트 크기 20, 굵게)
5. “그리기” 버튼을 클릭하면, 선택된 도형이 Canvas 위에 표시되어야 한다.
6. 이전 도형은 지워지고, 새로 선택한 도형만 표시되어야 한다. (힌트: canvas.delete("all") 활용)
'''

from tkinter import *

# 도형을 그리는 함수
def draw_shape():
    canvas.delete("all")  # 이전 그림 지우기
    choice = shape_var.get()
    
    if choice == 1:  # 사각형
        canvas.create_rectangle(50, 50, 150, 150, fill="red")
    elif choice == 2:  # 원(oval)
        canvas.create_oval(200, 80, 300, 180, fill="blue")
    elif choice == 3:  # 텍스트
        canvas.create_text(200, 150, text="Hello Duksung", fill="blue", font=("Helvetica", 20, "bold"))

# 메인 윈도우 생성
root = Tk()
root.title("중간고사 4번")
root.geometry("400x400")

# 캔버스
canvas = Canvas(root, width=400, height=300, bg="white")
canvas.pack()

# 라디오 버튼 선택값 저장 변수
shape_var = IntVar()
shape_var.set(1)  # 기본값: 사각형

# 라디오 버튼 생성
frame = Frame(root)
frame.pack(pady=10)

Radiobutton(frame, text="사각형", variable=shape_var, value=1).pack(side="left", padx=10)
Radiobutton(frame, text="원", variable=shape_var, value=2).pack(side="left", padx=10)
Radiobutton(frame, text="텍스트", variable=shape_var, value=3).pack(side="left", padx=10)

# 버튼 생성
Button(root, text="그리기", command=draw_shape, bg="lightgray").pack(pady=5)

root.mainloop()