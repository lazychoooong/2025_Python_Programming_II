class Student:
    def __init__(self, name, stu_id):
        self.name = name
        self.stu_id = stu_id
        self.att = 0

    def attend(self):
        self.att += 1

    def get_info(self):
        return f"{self.stu_id} {self.name} - 출석 {self.att} 회"
    
s1 = Student("김민수", "202501")
s2 = Student("이수정", "202502")

s1.attend()
s1.attend()
s2.attend()

print(s1.get_info)
print(s2.get_info)