class BankAccount(object):
    interest_rate = 0.3

    def __init__(self, name, number, balance):
        self.name = name
        self.number = number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("인출 성공")
        else:
            print("잔액 부족")

# 사용 예시
account = BankAccount("Kim", "123456789", 1000)
print("초기 잔고:", account.balance)
account.deposit(500)
print("저축 후 잔고:", account.balance)
account.withdraw(200)
print("인출 후 잔고:", account.balance)
account.withdraw(1500)  # 잔액 부족