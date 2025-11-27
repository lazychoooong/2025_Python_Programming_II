# 공이 찌그러지는 이유 : 공을 직접 그려서 이동시키고 있는데 속도가 못 따라가서...
# 직접 디벨롭하면서 차이를 알 수 있어야 함
from tkinter import *
import random
import time

root = Tk()
root.title("GAME")
root.resizable(0, 0)
root.wm_attributes("-topmost", 1)

canvas = Canvas(root, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
root.update()

class Ball:
    def __init__(self, canvas, paddle, color): # 공에 패들 추가
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.paddle = paddle
        self.canvas.move(self.id, 245, 100) # 공 시작 위치
        
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3

        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

        self.hit_bottom = False

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)

        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        print(self.canvas.coords(self.id))
        # 윗줄에서 저장한 정보 토대로 움직일 때마다 터미널에 출력

        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True

        if not self.hit_bottom:
            if self.hit_paddle(pos) == True:
                self.y = -3

        if self.hit_paddle(pos) == True:
            self.y = -3

        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3

    
class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)

        self.x = 0
        self.canvas_width = self.canvas.winfo_width()

        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def turn_left(self, evt):
        self.x = -2
        
    def turn_right(self, evt):
        self.x = 2

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)

        if pos[0] <= 0:
           self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0


paddle = Paddle(canvas, 'blue') 
ball = Ball(canvas, paddle, 'red')


while True:
    if ball.hit_bottom == False:
        ball.draw()
        paddle.draw()
    root.update_idletasks() # tkinter 내부 작업 처리
    root.update()
    time.sleep(0.01)

root.mainloop()