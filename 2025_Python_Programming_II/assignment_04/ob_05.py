# 05. 자동차 주행기록 프로그램 
class Car:
    def __init__(self, model):
        self.model = model
        self.odometer = 0

    def drive(self, km):
        self.odometer += km

    def info(self):
        print(f"모델 : {self.model}, 주행거리 : {self.odometer}")

c = Car("BMW")
c.drive(50)
c.drive(70)
c.info()