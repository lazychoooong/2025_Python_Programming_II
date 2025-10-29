'''
문제 5. __eq__ 메서드를 활용한 학번 로그인 프로그램
(※ 아래 그림 예시는 예시일 뿐이며, 레이아웃이나 색상은 동일하지 않아도 된다.)

1. 윈도우의 제목은 “중간고사 5번” 으로 한다.
2. 윈도우 크기는 300×160으로 한다.
3. Student 클래스를 정의한다.
- 멤버 변수: stu_id, name
- 생성자(__init__)에서 학번과 이름을 초기화한다.
- __eq__() 메서드를 재정의하여 학번이 같으면 동일한 학생으로 간주하도록 한다.
4. 다음과 같은 등록된 학생 객체 목록을 미리 생성한다.
students = [
    Student("202501", "김민수"),
    Student("202502", "이수정"),
    Student("202503", "박지훈")
]
5. tkinter를 이용하여 다음 GUI를 작성한다.
6. Label과 Entry를 이용하여 학번, 이름을 입력받는다.
7. “로그인” 버튼을 누르면 다음 기능이 수행된다:
- 입력한 학번과 이름으로 Student 객체를 생성한다.
- in 연산을 사용하여 해당 학생이 students 목록에 있는지 확인한다.
- 등록된 학번이면 “○○ 학생, 로그인 성공!”을 파란색으로 출력하고,
- 등록되지 않았으면 “등록되지 않은 학번입니다.”를 빨간색으로 출력한다.
- “취소” 버튼을 누르면 프로그램이 종료된다. (command=root.quit)

[힌트]
- __eq__() 메서드는 in 연산 시 자동으로 호출된다.
- 결과 메시지는 Label 위젯의 config() 메서드로 변경할 수 있다.
- grid() 배치 관리자를 사용한다.
'''
from tkinter import *

# --- Student 클래스 정의 ---
class Student:
    def __init__(self, stu_id, name):
        self.stu_id = stu_id
        self.name = name

    def __eq__(self, other):
        # Student 객체끼리만 비교 (학번이 같으면 같은 학생)
        if isinstance(other, Student):
            return self.stu_id == other.stu_id
        return False

# --- 등록된 학생 목록 ---
students = [
    Student("202501", "김민수"),
    Student("202502", "이수정"),
    Student("202503", "박지훈")
]

# --- 로그인 확인 함수 ---
def check_student():
    # 입력값 가져오기
    sid = e_id.get()
    name = e_name.get()
    user = Student(sid, name)  # 입력한 학번/이름으로 객체 생성

    if user in students:  # __eq__ 자동 호출됨
        result_label.config(text=f"{name} 학생, 로그인 성공!", fg="blue")
    else:
        result_label.config(text="등록되지 않은 학번입니다.", fg="red")

# --- 윈도우 설정 ---
root = Tk()
root.title("중간고사 5번")
root.geometry("250x150")

# --- 라벨 및 입력창 ---
Label(root, text="학번").grid(row=0, column=0, padx=10, pady=5)
Label(root, text="이름").grid(row=1, column=0, padx=10, pady=5)

e_id = Entry(root)
e_name = Entry(root)
e_id.grid(row=0, column=1, padx=10, pady=5)
e_name.grid(row=1, column=1, padx=10, pady=5)

# --- 버튼 ---
Button(root, text="로그인", command=check_student).grid(row=2, column=0, sticky=W, pady=8)
Button(root, text="취소", command=root.quit).grid(row=2, column=1, sticky=W, pady=8)

# --- 결과 출력 라벨 ---
result_label = Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2)

root.mainloop()