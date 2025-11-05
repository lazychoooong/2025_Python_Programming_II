# 07. 환율 계산 프로그램 만들기
class ExchangeRate:
    def __init__(self, currency, rate):
        self.currency = currency
        self.rate = rate

    def to_won(self, amount):
        return amount * self.rate
    
    def to_dollar(self, amount):
        return amount / self.rate

    def update_rate(self, new_rate):
        self.rate = new_rate
        print(f"USD 환율이 {self.rate}원으로 변경됨")
    
    def info(self):
        print(f"통화명 : {self.currency}, 현재 환율 : {self.rate}")

usd = ExchangeRate("USD", 1440)
usd.info()
print("100달러 =", usd.to_won(100), "원")
print("270000원 =", round(usd.to_dollar(270000), 2), "달러")

usd.update_rate(1400)
print("100달러 =", usd.to_won(100), "원")