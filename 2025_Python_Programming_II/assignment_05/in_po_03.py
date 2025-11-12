class Bird:
    def fly(self):
        print("새가 날고 있습니다.")

class Penguin(Bird):
    def fly(self):
        print("펭귄은 날지 못합니다.")

b = Bird()
p = Penguin()

b.fly()
p.fly()