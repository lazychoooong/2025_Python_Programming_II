class Rectangle:
    def __init__(self, height: int, width: int):
        self.height = height
        self.width = width
    
    def getArea(self) -> int:
        return self.height * self.width
    
    def resize(self, height: int, width: int):
        self.height = height
        self.width = width
    
rect = Rectangle(10, 20)
print("사각형의 넓이 :", rect.getArea())

rect.resize(5, 15)
print("변경 후 넓이 :", rect.getArea())