from tkinter import *
from PIL import ImageTk, Image
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def draw_image():
    global Img
    Img = PhotoImage(flie = "duksung.jpg")
    canvas.create_image(200, 150, anchor=NW, image=Img)



# 도형을 그리는 함수
def draw_shape():
    canvas.delete("all")  # 이전 그림 지우기
    choice = shape_var.get()
    
    if choice == 1:  # 사각형
        canvas.create_rectangle(50, 50, 150, 150, fill="red")
    elif choice == 2:  # 원(oval)
        canvas.create_oval(200, 80, 300, 180, fill="blue")
    elif choice == 3:  # 그림
        draw_image()
    elif choice == 4:  # 지우기
        canvas.delete("all")

# 메인 윈도우 생성
root = Tk()
root.title("중간고사 7번")
root.geometry("420x440")

# 캔버스
canvas = Canvas(root, width=400, height=320, bg="white")
canvas.pack()

# 라디오 버튼 선택값 저장 변수
shape_var = IntVar()
shape_var.set(1)  # 기본값: 사각형

# 라디오 버튼 생성
frame = Frame(root)
frame.pack(pady=10)

Radiobutton(frame, text="사각형", variable=shape_var, value=1).pack(side="left", padx=10)
Radiobutton(frame, text="원", variable=shape_var, value=2).pack(side="left", padx=10)
Radiobutton(frame, text="그림", variable=shape_var, value=3).pack(side="left", padx=10)
Radiobutton(frame, text="지우기", variable=shape_var, value=4).pack(side="left", padx=10)

# 버튼 생성
Button(root, text="그리기", command=draw_shape, bg="lightgray").pack(pady=5)

root.mainloop()