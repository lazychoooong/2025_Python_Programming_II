# 02. 온도 변환기 클래스 만들기
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        self.farhenheit = self.celsius * 1.8 + 32
        return self.farhenheit
    
t = Temperature(25)
print("섭씨 :", t.celsius)
print("화씨 :", t.to_fahrenheit())
