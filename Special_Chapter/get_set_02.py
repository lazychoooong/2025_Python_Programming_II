class Friend:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def getAge(self):
        return self.__age
    
    def setAge(self, age):
        if age >= 0:
            self.__age = age
        else:
            print("나이는 음수가 될 수 없습니다.")

x = Friend("홍길동", 20)
x.setAge(-5)
print(x.getAge())