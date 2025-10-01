import tkinter as tk

# 기본 윈도우 생성
root = tk.Tk()
root.title("Tkinter 예제") # 창 제목
root.geometry("200x100") # 창 크기 설정 (가로 200, 세로 100)

# 라벨 (Label) 하나 추가
label = tk.Label(root,text = "Hello, Tkinter!")
label.pack(pady = 20)

# 이벤트 루프 실행
root.mainloop()