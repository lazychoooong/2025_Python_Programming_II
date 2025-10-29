'''
문제 3. 상속을 이용한 학생 정보 프로그램 

1. 상위 클래스 Student 를 정의한다.
- 멤버 변수: stu_id, name
- 생성자(__init__)를 이용해 학번과 이름을 초기화한다.
- 메서드 show_info()를 작성하여 다음 형식으로 출력한다.
- 예시 : 학번: 202501, 이름: 김민수

2. 하위 클래스 UndergraduateStudent 와 GraduateStudent 를 정의한다.
- 두 클래스는 Student 클래스를 상속받는다.

- UndergraduateStudent 클래스는 major(전공)을 멤버로 가진다.
- introduce() 메서드에서 다음과 같이 출력한다.
- 예시 : 저는 학부생 김민수입니다. 전공은 컴퓨터공학과입니다.

- GraduateStudent 클래스는 advisor(지도교수)를 멤버로 가진다.
- introduce() 메서드에서 다음과 같이 출력한다.
- 저는 대학원생 이수정입니다. 지도교수님은 홍길동입니다.

3. 다음 객체를 생성하고 메서드를 호출한다.
u1 = UndergraduateStudent("202501", "김민수", "컴퓨터공학과")
g1 = GraduateStudent("202401", "이수정", "홍길동")

u1.show_info()
u1.introduce()

g1.show_info()
g1.introduce()

[출력 예시]
학번: 202501, 이름: 김민수
저는 학부생 김민수입니다. 전공은 컴퓨터공학과입니다.
학번: 202401, 이름: 이수정
저는 대학원생 이수정입니다. 지도교수님은 홍길동입니다.
'''
# 상위 클래스
class Student:
    def __init__(self, stu_id, name):
        self.stu_id = stu_id
        self.name = name

    def show_info(self):
        print(f"학번: {self.stu_id}, 이름: {self.name}")


# 하위 클래스 1: 학부생
class UndergraduateStudent(Student):
    def __init__(self, stu_id, name, major):
        super().__init__(stu_id, name)
        self.major = major

    def introduce(self):
        print(f"저는 학부생 {self.name}입니다. 전공은 {self.major}입니다.")


# 하위 클래스 2: 대학원생
class GraduateStudent(Student):
    def __init__(self, stu_id, name, advisor):
        super().__init__(stu_id, name)
        self.advisor = advisor

    def introduce(self):
        print(f"저는 대학원생 {self.name}입니다. 지도교수님는 {self.advisor}입니다.")


# 실행 예시
stu1 = UndergraduateStudent("202501", "김민수", "컴퓨터공학과")
stu2 = GraduateStudent("202401", "이수정", "홍길동")

stu1.show_info()
stu1.introduce()

stu2.show_info()
stu2.introduce()