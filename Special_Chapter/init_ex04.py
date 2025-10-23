class Student:
    def attend(self):
        self.att += 1

    def get_info(self):
        return f"{self.stu_id} {self.name} - 출석 {self.att} 회"

s1, s2 = Student(), Student()
s1.name, s1.stu_id, s1.att = "김민수", "202501", 0
s2.name, s2.stu_id, s2.att = "이수정", "202502", 0

s1.attend()
s1.attend()
s2.attend()

print(s1.get_info())
print(s2.get_info())