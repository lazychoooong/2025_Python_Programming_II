class Student:
    def __init__(self, stu_id, name):
        self.stu_id = stu_id
        self.name = name

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.stu_id == other.stu_id
        return False

s1 = Student("202501", "김민수")
s2 = Student("202502", "이수정")
s3 = Student("202503", "박지훈")
s4 = Student("202501", "홍길동")

students = [s1, s2, s3]

print(s1 in students)
print(s2 in students)
print(s3 in students)
print(s4 in students)