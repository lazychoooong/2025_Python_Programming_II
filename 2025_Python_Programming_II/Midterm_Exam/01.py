'''
문제 1. DSstudent 클래스를 만들고, 자신의 학번과 이름을 출력하는 프로그램을 작성하시오.

1. DSstudent 클래스를 정의한다.
- 멤버 변수: stu_id, name
- 생성자(__init__)에서 학번과 이름을 초기화한다.
- show_info() 메서드를 작성하여 학번과 이름을 출력한다.
학번: 202501, 이름: 김덕성

2. 자신의 학번과 이름을 사용하여 객체를 생성하고,
show_info() 메서드를 호출하여 정보를 출력한다.
'''

class DSstudent:
    def __init__(self, stu_id, name):
        self.stu_id = stu_id
        self.name = name

    def show_info(self):
        print(f"학번: {self.stu_id}, 이름: {self.name}")


# 실행 예시
student1 = DSstudent("202501", "김덕성")
student1.show_info()