# 04. 과목 성적 관리 클래스
class Course:
    def __init__(self, name):
        self.name = name
        self.scores = []

    def add_scores(self, s):
        self.scores.append(s)

    def avg(self):
        if len(self.scores) > 0:
            return sum(self.scores) / len(self.scores)
        else:
            print("점수 합계 결과가 음수이므로 결과를 출력할 수 없습니다.")
        
    
    def info(self):
        print(f"과목 : {self.name}, 평균 : {self.avg()}")

c = Course("파이썬")
c.add_scores(80)
c.add_scores(90)
print(c.info())


