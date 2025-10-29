class Student:
    def __init__(self, name):
        self.name = name
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)
        print(f"{self.name}의 성적 {score}점이 추가되었습니다.")

    def cal_avg(self):
        if not self.scores:
            return 0
        return sum(self.scores) / len(self.scores)

# 학생 인스턴스 생성
student = Student("Kim")

# 성적 추가
student.add_score(90)
student.add_score(85)
student.add_score(78)

# 평균 성적 출력
avg = student.cal_avg()
print(f"{student.name}의 평균 성적: {avg:.2f}")