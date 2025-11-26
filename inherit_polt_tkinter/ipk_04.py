import tkinter as tk

class Person:
    def __init__(self, name: str):
        self.name = name

class Student(Person):
    def __init__(self, name: str):
        super().__init__(name)
        self.classes = []  

    def enrollCourse(self, subject: str):
        if subject not in self.classes:
            self.classes.append(subject)

    def clearCourses(self):
        self.classes.clear()

root = tk.Tk()
root.title("문제 4")
root.geometry("380x280")

stu = Student("홍길동") 
title = tk.Label(root, text=f"학생: {stu.name}", font=("맑은 고딕", 11, "bold"))
title.pack(pady=6)

frm = tk.Frame(root)
frm.pack(pady=8, anchor="center")


var_py  = tk.IntVar(value=0)
var_ai  = tk.IntVar(value=0)
var_ds  = tk.IntVar(value=0)


cb1 = tk.Checkbutton(frm, text="Python",      variable=var_py)
cb2 = tk.Checkbutton(frm, text="AI",          variable=var_ai)
cb3 = tk.Checkbutton(frm, text="DataScience", variable=var_ds)

cb1.grid(row=0, column=0, padx=8, pady=4)
cb2.grid(row=0, column=1, padx=8, pady=4)
cb3.grid(row=0, column=2, padx=8, pady=4)


result = tk.StringVar(value="과목을 선택하고 [등록하기]를 누르세요.")
lb = tk.Label(root, textvariable=result, wraplength=340, justify="left")
lb.pack(pady=8)


def register_courses():
    stu.clearCourses()
    if var_py.get(): stu.enrollCourse("Python")
    if var_ai.get(): stu.enrollCourse("AI")
    if var_ds.get(): stu.enrollCourse("DataScience")

    if stu.classes:
        result.set(f"등록된 과목: {', '.join(stu.classes)}")
    else:
        result.set("선택된 과목이 없습니다.")

def reset_all():
    var_py.set(0); var_ai.set(0); var_ds.set(0)
    stu.clearCourses()
    result.set("모든 선택을 해제했습니다.")


btn_frame = tk.Frame(root)
btn_frame.pack(pady=6)

tk.Button(btn_frame, text="등록하기", command=register_courses).pack(side="left", padx=8)
tk.Button(btn_frame, text="초기화",   command=reset_all).pack(side="left", padx=8)

root.mainloop()