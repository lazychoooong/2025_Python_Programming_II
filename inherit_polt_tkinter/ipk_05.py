import tkinter as tk

class Pet:
    def __init__(self, name):
        self.name = name

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
root.title("문제 5")
root.geometry("700x300")

person = Person("홍길동")


tk.Label(root, text="반려동물 등록하기", font=("맑은 고딕", 13, "bold")).pack(pady=8)


frm_main = tk.Frame(root)
frm_main.pack(pady=10)


tk.Label(frm_main, text="반려동물 이름:", width=15, anchor="e").grid(row=0, column=0, padx=5, pady=5)
pet_name_entry = tk.Entry(frm_main, width=25)
pet_name_entry.grid(row=0, column=1, columnspan=3, padx=5, pady=5, sticky="w")


tk.Label(frm_main, text="종류:", width=15, anchor="e").grid(row=1, column=0, padx=5, pady=5)
pet_type = tk.StringVar(value="Dog")
tk.Radiobutton(frm_main, text="강아지", value="Dog", variable=pet_type).grid(row=1, column=1, padx=5, sticky="w")
tk.Radiobutton(frm_main, text="고양이", value="Cat", variable=pet_type).grid(row=1, column=2, padx=5, sticky="w")


tk.Label(frm_main, text="옵션:", width=15, anchor="e").grid(row=2, column=0, padx=5, pady=5)
vaccinated = tk.IntVar(value=0)
neutered = tk.IntVar(value=0)
tk.Checkbutton(frm_main, text="예방접종 완료", variable=vaccinated).grid(row=2, column=1, padx=5, sticky="w")
tk.Checkbutton(frm_main, text="중성화 완료", variable=neutered).grid(row=2, column=2, padx=5, sticky="w")


result_var = tk.StringVar(value="등록 정보를 확인하세요.")
tk.Label(frm_main, textvariable=result_var, fg="blue", wraplength=500, justify="left").grid(row=3, column=0, columnspan=4, pady=15)


def register():
    pet_name = pet_name_entry.get() or "이름없음"
    kind = pet_type.get()
    pet = Dog(pet_name) if kind == "Dog" else Cat(pet_name)
    person.pet = pet

    vac = "O" if vaccinated.get() else "X"
    neu = "O" if neutered.get() else "X"
    kind_kor = "강아지" if kind == "Dog" else "고양이"

    msg = (f"{person.name}의 반려동물 등록 완료!\n"
           f"이름: {pet.name} ({kind_kor})\n"
           f"소리: {pet.speak()}\n"
           f"예방접종: {vac}, 중성화: {neu}")
    result_var.set(msg)

def reset():
    pet_name_entry.delete(0, tk.END)
    pet_type.set("Dog")
    vaccinated.set(0)
    neutered.set(0)
    person.pet = None
    result_var.set("등록 정보를 확인하세요.")


frm_btn = tk.Frame(root)
frm_btn.pack(pady=5)
tk.Button(frm_btn, text="등록하기", width=12, command=register).pack(side="left", padx=15)
tk.Button(frm_btn, text="초기화", width=12, command=reset).pack(side="left", padx=15)

root.mainloop()