# 과제 1
class Car:
    def __init__(self, speed):
        self.speed = speed

    def get_speed(self):
        return (f"현재 속도 : {self.speed}km/h")

class SportsCar(Car):
    def __init__(self, speed, turbo):
        super().__init__(speed)
        self.turbo = turbo

    def get_speed(self):
        if self.turbo:
            return "현재 속도 : 200km/h (터보 ON)"
        else:
            return "현재 속도 : 100km/h (터보 OFF)"

car1 = Car(80)
print(car1.get_speed())

sport1 = SportsCar(150, True)
print(sport1.get_speed())

sport2 = SportsCar(120, False)
print(sport2.get_speed())