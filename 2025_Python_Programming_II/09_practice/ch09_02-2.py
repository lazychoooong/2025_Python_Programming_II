class Dog:
    def __init__(self, name, age, tricks):
        self.name = name
        self.age = age
        self.tricks = tricks

    def bark(self):
        print(f"{self.name}가 짖고 있습니다!")

    def show_tricks(self):
        tricks_str = '", "'.join(self.tricks) #join() 리스트의 요소들을 하나의 문자열로 연결
        print(f'{self.name}의 장기는 "{tricks_str}" 입니다.')

# 강아지 인스턴스 생성
dog1 = Dog("바둑이", 3, ["뒹굴기", "달리기"])
dog2 = Dog("멍멍이", 5, ["먹기"])

# 강아지의 장기 출력
dog1.show_tricks()
dog2.show_tricks()