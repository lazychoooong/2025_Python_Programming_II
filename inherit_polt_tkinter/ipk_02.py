import tkinter as tk

class Pet:
    def speak(self):
        return "..."

class Dog(Pet): 
    def speak(self):
        return "멍멍!"

class Cat(Pet): 
    def speak(self):
        return "야옹!"

class Person:
    def __init__(self, name, pet=None):
        self.name = name
        self.pet = pet  


root = tk.Tk()
root.title("문제2")
root.geometry("400x200")


tk.Label(root, text="동물을 선택해 주세요.", font=("맑은 고딕", 12)).pack(pady=10)


person = Person("홍길동")


def select_dog():
    person.pet = Dog() 
    result.set("강아지를 선택했습니다.")

def select_cat():
    person.pet = Cat()
    result.set("고양이를 선택했습니다.")

def speak():
    result.set(f"{person.name}의 반려동물 → {person.pet.speak()}")


frame = tk.Frame(root)
frame.pack(pady=10)

tk.Button(frame, text="강아지 선택", command=select_dog).pack(side="left", padx=8)
tk.Button(frame, text="고양이 선택", command=select_cat).pack(side="left", padx=8)
tk.Button(root, text="말하기", command=speak).pack(pady=10)


result = tk.StringVar(value="")
speak_label = tk.Label(root, textvariable=result, font=("맑은 고딕", 12), fg="blue")
speak_label.pack(pady=10)


root.mainloop()