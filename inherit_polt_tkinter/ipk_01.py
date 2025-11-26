import tkinter as tk

class Vehicle:
    def __init__(self, name):
        self.name = name
    def drive(self):
        raise NotImplementedError("이것은 추상 메소드입니다.") 

class Car(Vehicle):
    def drive(self):
        return f"승용차 {self.name}가 주행합니다."

class Truck(Vehicle):
    def drive(self):
        return f"트럭 {self.name}가 화물을 싣고 주행합니다."


car = Car("car1")
truck = Truck("truck1")


root = tk.Tk()
root.title("문제1")
root.geometry("400x300")


label1 = tk.Label(root, text="버튼을 눌러보세요.", font=("맑은 고딕", 11))
label1.pack(pady=10)


frame = tk.Frame(root)
frame.pack(pady=10)


def show_car():
    result.set(car.drive())

def show_truck():
    result.set(truck.drive())

tk.Button(frame, text="자동차 주행", command=show_car).pack(side="left", padx=10)
tk.Button(frame, text="트럭 주행", command=show_truck).pack(side="left", padx=10)

result = tk.StringVar(value="")
label2 = tk.Label(root, textvariable=result, font=("맑은 고딕", 11))
label2.pack(pady=10)

root.mainloop()