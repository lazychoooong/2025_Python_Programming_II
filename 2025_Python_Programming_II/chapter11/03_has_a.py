class Animal(object):
    pass

class Dog(Animal):
    def __init__(self, name):
        self.name = name

class Person(object):
    def __init__(self, name):
        self.name = name
        self.pet = None # 미리 저장 안 했는데 사용 가능...?
# 파이썬은 유용한 사용이 가능하기 때문. 값이 없어서 임의대로 설정하고 사용
    
dog1 = Dog("dog1")
person1 = Person("홍길동")
person1.pet = dog1