import tkinter as tk
import random
import time

def animate_text(canvas, text_id):
    for _ in range(100):
        update_text_size(canvas, text_id) #글자 크기 변경
        update_text_color(canvas, text_id) #글자 색상 변경
        canvas.update() #변경 사항 즉시 반영
        time.sleep(0.5) #0.5초 대기 (애니메이션 효과)

def update_text_size(canvas, text_id):
    current_size = 100
    new_size = current_size + random.randint(-100, 100)
    canvas.itemconfigure(text_id, font=("Helvetica", new_size))
    #canvas.itemconfigure(text_id, fill=new_color)
    #Tkinter 캔버스(Canvas)에 이미 그려진 객체의 속성을 변경하는 함수

def update_text_color(canvas, text_id):
    colors = ["red", "green", "blue", "orange", "purple", "pink", "cyan", "yellow"]
    new_color = random.choice(colors)
    canvas.itemconfigure(text_id, fill=new_color)

# 애플리케이션 초기 설정
root = tk.Tk()
root.title("Text Animation")

canvas = tk.Canvas(root, width=400, height=200)
canvas.pack()

text_id = canvas.create_text(200, 100, text="Hello", font=("Helvetica", 12), fill="black")

# 애니메이션 실행
animate_text(canvas, text_id)

# 애플리케이션 실행
root.mainloop()