# 01. 도서 대출 관리 프로그램
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.borrowed = False
    
    def borrow(self):
        if not self.borrowed:
            self.borrowed = True
            print(f"{self.title}이(가) 대출되었습니다.")
        else:
            print(f"{self.title}은(는) 이미 대출 중입니다.")


    def return_book(self):
        if self.borrowed:
            self.borrowed = False
            print(f"{self.title}이(가) 반납되었습니다.")
        else:
            borrowed = False

b1 = Book("파이썬 프로그래밍", "홍길동")
b1.borrow()
b1.borrow()
b1.return_book()
