import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def plot_graph():
    x = float(x_entry.get()) #Entry위젯에서 문자열을 꺼내 숫자(float)로 변환
    y = float(y_entry.get())
    x_data.append(x) #데이터 누적
    y_data.append(y)
    ax.clear() #기존 그래프 지우기
    ax.plot(x_data, y_data, marker='o', linestyle='-') #새로운 데이터로 선 그래프 그리기
    canvas.draw() #캔버스 업데이트


# 애플리케이션 초기 설정
root = tk.Tk()
root.title("Dynamic Line Graph")

x_data = []
y_data = [] #좌표 데이터 저장할 리스트

x_label = tk.Label(root, text="Enter x coordinate:") #좌표 입력
x_label.pack()
x_entry = tk.Entry(root)
x_entry.pack()

y_label = tk.Label(root, text="Enter y coordinate:") #y좌표 입력
y_label.pack()
y_entry = tk.Entry(root)
y_entry.pack()

plot_button = tk.Button(root, text="Plot", command=plot_graph) #버튼생성
plot_button.pack()

#Matplotlib Figure 생성
fig = Figure(figsize=(5, 4), dpi=100) #해상도 지원
ax = fig.add_subplot(111)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

# 애플리케이션 실행
root.mainloop()