class Vehicle:
    def drive(self):
        pass

class Truck(Vehicle):
    def drive(self):
        return "트럭이 화물을 운송합니다."
    
class Car(Vehicle):
    def drive(self):
        return "승용차가 사람을 태우고 있습니다."

vehicles = [Truck(), Car(), Truck()]

for v in vehicles:
    print(v.drive())