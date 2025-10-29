import tkinter as tk
import random

class MovingShapeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Moving Shape App")

        # 캔버스 생성
        self.canvas = tk.Canvas(root, width=600, height=600, bg="white")
        self.canvas.pack()

        # 원 생성
        self.shape = self.canvas.create_oval(100, 100, 200, 200, fill="blue")

        # 키보드 이벤트 바인딩
        self.root.bind("<Up>", self.move_up)
        self.root.bind("<Down>", self.move_down)
        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)

        # 마우스 이벤트 바인딩
        self.canvas.bind("<B1-Motion>", self.change_color)

    # ===== 도형 이동 관련 메서드 =====
    def move_shape(self, dx, dy):
        self.canvas.move(self.shape, dx, dy)

    def move_up(self, event):
        self.move_shape(0, -10)

    def move_down(self, event):
        self.move_shape(0, 10)

    def move_left(self, event):
        self.move_shape(-10, 0)

    def move_right(self, event):
        self.move_shape(10, 0)

    # ===== 색상 변경 메서드 =====
    def change_color(self, event):
        colors = ["red", "orange", "yellow", "green", "blue", "purple"]
        color = random.choice(colors)
        self.canvas.itemconfig(self.shape, fill=color)


# 프로그램 실행
root = tk.Tk()
app = MovingShapeApp(root)
root.mainloop()