class Animal:
    def speak(self):
        print("동물이 소리를 냅니다.")

class Dog:
    def __init__(self):
        self.animal = Animal()

    def speak(self):
        self.animal.speak() # 상속받은 것이 아닌, 가져와서 쓰는 개념
        print("멍멍!") 

dog = Dog()
dog.speak()

#4번, 5번 is a - has a 구분 확실히 해야 함!