# 분명 라벨 설정 구조상 tkinter 창에 떠야 하는데
# tk_01.py 파일을 실행했을 때 대출/반납 결과가 자꾸 터미널에만 떠서
# 인터넷에 검색해 보고 StringVar를 사용한 버전을 추가로 첨부했습니다! 감사합니다.
from tkinter import *

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.borrowed = False

    def borrow(self):
        if not self.borrowed:
            self.borrowed = True
            return f"{self.title}이(가) 대출되었습니다."
        else:
            return f"{self.title}은(는) 이미 대출 중입니다."

    def return_book(self):
        if self.borrowed:
            self.borrowed = False
            return f"{self.title}이(가) 반납되었습니다."
        else:
            return f"{self.title}은(는) 대출되지 않은 상태입니다."

def borrow_book():
    title = entry_title.get().strip()
    author = entry_author.get().strip()

    if not title or not author:
        result_var.set("제목과 저자를 모두 입력하세요.")
        label_result.config(fg="red")
        return

    global book
    book = Book(title, author)

    msg = book.borrow()
    result_var.set(msg)
    label_result.config(fg="blue")

def return_book():
    try:
        msg = book.return_book()
        result_var.set(msg)
        label_result.config(fg="green")
    except NameError:
        result_var.set("먼저 도서를 대출하세요.")
        label_result.config(fg="red")


root = Tk()
root.title("도서 대출 관리 프로그램")
root.geometry("400x400")

Label(root, text="도서 대출 관리 시스템", font=("Arial", 13, "bold")).pack(pady=8)


frame_input = Frame(root)
frame_input.pack(pady=5)

Label(frame_input, text="제목:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_title = Entry(frame_input, width=28)
entry_title.grid(row=0, column=1, padx=5, pady=5)

Label(frame_input, text="저자:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_author = Entry(frame_input, width=28)
entry_author.grid(row=1, column=1, padx=5, pady=5)

frame_btn = Frame(root)
frame_btn.pack(pady=10)

Button(frame_btn, text="대출", width=10, command=borrow_book).pack(side="left", padx=10)
Button(frame_btn, text="반납", width=10, command=return_book).pack(side="left", padx=10)

result_var = StringVar(value="")
label_result = Label(root, textvariable=result_var, font=("Arial", 11))
label_result.pack(pady=8)


entry_title.focus_set()
root.mainloop()