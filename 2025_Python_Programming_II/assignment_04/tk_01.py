# 01. 도서관리 프로그램-v1
from tkinter import *

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.borrowed = False

    def borrow(self):
        if not self.borrowed:
            self.borrowed = True
            return print(f"{self.title}이(가) 대출되었습니다.")
        else:
            return print(f"{self.title}은(는) 이미 대출 중입니다.")

    def return_book(self):
        if self.borrowed:
            self.borrowed = False
            return print(f"{self.title}이(가) 반납되었습니다.")
        else:
            return print(f"{self.title}은(는) 대출되지 않은 상태입니다.")

def borrow_book():
    title = entry_title.get()
    author = entry_author.get()

    if title == "" or author == "":
        label_result.config(text="제목과 저자를 모두 입력해 주세요.", fg="red")
        return
    
    global book
    book = Book(title, author)
    msg = book.borrow()
    label_result.config(text=msg, fg="blue")

def return_book():
    try:
        msg = book.return_book()
        label_result.config(text=msg, fg="green")
    except NameError:
        label_result.config(text="먼저 도서를 대출하세요.", fg="red")

root = Tk()
root.title("도서 대출 관리 프로그램")
root.geometry("400x400")

Label(root, text = "도서 대출 관리 시스템", font=("Arial", 13, "bold")).pack(pady = 8)

frame_input = Frame(root)
frame_input.pack(pady=5)

Label(frame_input, text = "제목 :").grid(row=0, column=0, padx=5, pady=5)
entry_title = Entry(frame_input, width=25)
entry_title.grid(row=0, column=1, padx=5, pady=5)

Label(frame_input, text = "저자 :").grid(row=1, column=0, padx=5, pady=5)
entry_author = Entry(frame_input, width=25)
entry_author.grid(row=1, column=1, padx=5, pady=5)

frame_button = Frame(root)
frame_button.pack(pady=10)

Button(frame_button, text="대출", width=10, command=borrow_book).pack(side="left", padx=10)
Button(frame_button, text="반납", width=10, command=return_book).pack(side="left", padx=10)

label_result = Label(root, text="", font=("Arial", 11))
label_result.pack(pady=5)

root.mainloop()
