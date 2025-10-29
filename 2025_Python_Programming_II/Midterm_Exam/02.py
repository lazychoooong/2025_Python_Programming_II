'''
문제 2. 접근자 / 설정자를 이용한 계좌 관리 프로그램

1. BankAccount 클래스를 정의한다.
- 인스턴스 변수 __balance 를 사용하여 각 계좌별로 잔액을 관리한다.
- 생성자(__init__)는 계좌의 이름(owner)을 매개변수로 받아 저장하고,
  "A 계좌가 생성되었습니다." 와 같은 문구를 출력한다.

2. 접근자(getter) 와 설정자(setter) 를 구현한다.
- get_balance() : 현재 잔액을 반환한다.
- set_balance(amount) : 잔액을 직접 수정하되, 0 이상인 값만 허용한다.

3. 입금(deposit) 과 출금(withdraw) 메서드를 작성한다.
- deposit(amount) : 0보다 큰 금액만 입금 가능
- withdraw(amount) : 잔액보다 많은 금액은 출금 불가

4. 각각 실행 시 아래와 같은 문구를 출력한다.
A 통장에 100원이 입금되었습니다.
B 통장에서 30원이 출금되었습니다.

5. 다음 코드를 실행했을 때 예시와 같은 출력이 나타나도록 하시오.

a = BankAccount("A")
b = BankAccount("B")

a.deposit(100)
b.deposit(200)
a.withdraw(30)
b.withdraw(50)

print(f"{a.owner}계좌의 현재 잔액:", a.get_balance())
print(f"{b.owner}계좌의 현재 잔액:", b.get_balance())

a.set_balance(500)
print(f"{a.owner}계좌의 수정된 잔액:", a.get_balance())

'''
class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.__balance = 0  # 인스턴스 변수 (각 계좌별로 관리)
        print(f"{self.owner} 계좌가 생성되었습니다.")

    # 접근자 (Getter)
    def get_balance(self):
        return self.__balance

    # 설정자 (Setter)
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("잔액은 음수가 될 수 없습니다.")

    # 입금 메서드
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{self.owner} 통장에 {amount}원이 입금되었습니다.")
        else:
            print(f"{self.owner} 계좌에 잘못된 금액이 입력되었습니다.")
        return self.__balance

    # 출금 메서드
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"{self.owner} 통장에서 {amount}원이 출금되었습니다.")
        else:
            print(f"{self.owner} 계좌의 잔액이 부족하거나 잘못된 금액입니다.")
        return self.__balance


# 실행 예시
a = BankAccount("A")
b = BankAccount("B")

a.deposit(100)
b.deposit(200)
a.withdraw(30)
b.withdraw(50)

print(f"{a.owner} 계좌의 현재 잔액:", a.get_balance())
print(f"{b.owner} 계좌의 현재 잔액:", b.get_balance())

a.set_balance(500)
print(f"{a.owner} 계좌의 수정된 잔액:", a.get_balance())