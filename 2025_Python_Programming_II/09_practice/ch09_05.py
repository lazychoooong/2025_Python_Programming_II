class Employee:
    # 클래스 변수 초기화
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        # 새로운 직원이 추가될 때마다 empCount를 증가시킴
        Employee.empCount += 1

    def displayEmp(self):
        print("Name:", self.name + ",", "Salary:", self.salary)

# Employee 객체 생성
emp1 = Employee("Kim", 5000)
emp2 = Employee("Lee", 6000)

# 직원 정보 출력
emp1.displayEmp()
emp2.displayEmp()

# 전체 직원 수 출력
print("Total employees:", Employee.empCount)