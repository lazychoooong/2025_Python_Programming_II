class Computer:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def get_info(self):
        return f"브랜드: {self.brand}, 가격: {self.price}만 원"

class Laptop(Computer):
    def __init__(self, brand, price, weight):
        super().__init__(brand, price)
        self.weight = weight

    def get_info(self):
        return f"브랜드: {self.brand}, 가격: {self.price}만 원, 무게: {self.weight}kg"

com = Computer("삼성", 120)
lap = Laptop("LG", 150, 1.5)

print(com.get_info())
print(lap.get_info())