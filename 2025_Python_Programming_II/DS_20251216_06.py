class Inventory:
    def __init__(self, stock):
        self.__stock = 0
        print("새 상품이 등록되었습니다.")

    # 접근자 (Getter)
    def get_stock(self):
        return self.__stock

    # 설정자 (Setter)
    def set_stock(self, amount):
        if amount >= 0:
            self.__stock = amount
        else:
            print("재고 수량은 0 이상이어야 합니다.")

    # 입고 메서드
    def add_stock(self, amount):
        if amount > 0:
            self.__stock += amount
            print(f"{amount}개가 입고되었습니다.")
        else:
            print("0보다 큰 수량만 입고 가능합니다.")
        return self.__stock

    # 출고 메서드
    def remove_stock(self, amount):
        if 0 < amount <= self.stock:
            self.__stock -= amount
            print(f"{amount}개가 출고되었습니다.")
        else:
            print(f"현재 재고보다 많은 수량은 출고 불가능합니다.")
        return self.__stock


# 실행 예시
item1 = Inventory()
item1.add_stock(10)
item1.remove_stock(3)
print("현재 재고 수량 :", item1.get_stock())

item1.set_stock(10)
print("수정된 재고 수량 :", item1.get_stock())