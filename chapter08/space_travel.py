import tkinter as tk
import random

# 별 생성 함수
def create_star(canvas, x, y, radius):
    return canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill="white", outline="")

# 우주선 생성 함수
def create_spacecraft(canvas, x, y, image):
    return canvas.create_image(x, y, image=image)

# 우주선 이동 함수
def move_spacecraft(canvas, obj_id, dx, dy):
    canvas.move(obj_id, dx, dy)

# 우주선 애니메이션 함수
def animate_spacecraft():
    x, y = canvas.coords(spacecraft)
    if x < -50 or x > window_width + 50 or y < -50 or y > window_height + 50:
        reset_spacecraft()
    else:
        move_spacecraft(canvas, spacecraft, dx, dy)
    window.after(200, animate_spacecraft)

# 우주선 리셋 함수
def reset_spacecraft():
    global dx, dy
    x = random.randint(0, window_width)
    y = random.randint(0, window_height)
    dx = random.randint(0, 30)
    dy = random.randint(-30, 0)
    canvas.coords(spacecraft, x, y)

window = tk.Tk()
window.title("우주 여행 애니메이션")
window_width = 800
window_height = 600

canvas = tk.Canvas(window, width=window_width, height=window_height, bg="black")
canvas.pack()

# 우주선 이미지 로드
spacecraft_image = tk.PhotoImage(file="chapter08\spaceship.png")

# 별들 생성
stars = []
for _ in range(50):
    x = random.randint(0, window_width)
    y = random.randint(0, window_height)
    radius = random.randint(1, 10)
    stars.append(create_star(canvas, x, y, radius))

# 우주선 생성
x = random.randint(0, window_width)
y = random.randint(0, window_height)
spacecraft = create_spacecraft(canvas, x, y, image=spacecraft_image)
dx = random.randint(0, 30)
dy = random.randint(-30, 0)

# 우주선 애니메이션 시작
animate_spacecraft()
window.mainloop()