# 1. Dog is an Animal
class Animal:
    def move(self):
        print("동물이 움직입니다.")

class Dog(Animal):
    def move(self):
        super().move()
        print("개가 달립니다.")

dog = Dog()
dog.move()

# 2. Student is a Person
class Person:
    def speak(self):
        print("사람이 말을 합니다.")

class Student(Person):
    def study(self):
        print("학생이 공부합니다.")

stu = Student()
stu.speak()
stu.study()

# 3. Car is a Vehicle
class Vehicle:
    def drive(self):
        print("차량이 이동 중입니다.")
        
class Car(Vehicle):
    def drive(self):
        super().drive()
        print("자동차가 도로를 달립니다.")

car = Car()
car.drive()

# 4. Manager is an Employee
class Employee:
    def work(self):
        print("직원이 일합니다.")
        
class Manager(Employee):
    def work(self):
        super().work()
        print("관리자가 팁을 관리합니다.")

m = Manager()
m.work()

# 5. Penguin is a Bird
class Bird:
    def fly(self):
        print("새가 날아갑니다.")

class Penguin(Bird):
    def fly(self):
        super().fly()
        print("펭귄은 날지 못하지만 수영을 합니다.")

p = Penguin()
p.fly()