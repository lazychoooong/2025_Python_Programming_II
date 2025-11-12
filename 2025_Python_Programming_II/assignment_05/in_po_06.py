import tkinter as tk

class Animal:
    def speak(self):
        return "..."  # 기본값

class Dog(Animal):
    def speak(self):
        return "멍멍!"

class Cat(Animal):
    def speak(self):
        return "야옹!"

class Duck(Animal):
    def speak(self):
        return "꽥꽥!"


def make_sound(animal: Animal):
    sound = animal.speak()
    result_label.config(text=sound)  

root = tk.Tk()
root.title("동물 소리 듣기")
root.geometry("360x180")
root.resizable(False, False)

tk.Label(root, text="동물 버튼을 눌러 소리를 들어보세요.").pack(pady=(12, 6))


btns = tk.Frame(root)
btns.pack(pady=4)

tk.Button(btns, text="강아지", width=10, command=lambda: make_sound(Dog())).pack(side="left", padx=6)
tk.Button(btns, text="고양이", width=10, command=lambda: make_sound(Cat())).pack(side="left", padx=6)
tk.Button(btns, text="오리", width=10, command=lambda: make_sound(Duck())).pack(side="left", padx=6)

result_label = tk.Label(root, text="(여기에 울음소리가 나옵니다)", font=("맑은 고딕", 14, "bold"))
result_label.pack(pady=16)

root.mainloop()