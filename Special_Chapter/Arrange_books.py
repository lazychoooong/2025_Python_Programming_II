'''
도서관리 프로그램-v1
1. Book 클래스 정의
- title : 도서 제목
- author : 저자
- borrowed : 대출 여부(True 또는 False, 기본값은 False)
- 생성자 (__init__) : 제목과 저자를 매개변수로 받아 초기화한다.대출 상태(borrowed)는 기본값 False로 설정한다.

2. 메서드 정의
- borrow(): 도서가 대출되지 않은 상태라면 대출 상태로 변경하고, "책제목이(가) 대출되었습니다." 문장을 반환한다.
- 이미 대출 중이라면 "책제목"은(는) 이미 대출 중입니다. 문장을 반환한다.
- return_book()	대출 중인 도서를 반납 상태로 바꾸고, "책제목이(가) 반납되었습니다." 문장을 반환한다.
- 대출되지 않은 도서를 반납하려 하면 "책제목은(는) 대출되지 않은 상태입니다." 문장을 반환한다.

3. Tkinter GUI 구현
- 다음 조건에 맞는 그래픽 인터페이스(GUI) 를 작성하시오.
- 프로그램 제목: "도서 대출 관리 프로그램"
- 입력 항목:Entry 위젯 2개 (제목, 저자)
- 버튼: "대출" 버튼: 입력한 책을 Book 객체로 생성하고 borrow() 실행
- "반납" 버튼: 이미 대출된 책의 return_book() 실행
- 결과 출력: 결과 메시지를 Label 위젯을 통해 화면에 표시
예: "데이터사이언스입문이(가) 대출되었습니다."
'''
from tkinter import *

#Book 클래스 정의
class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author
    self.borrowed = False  # 대출 상태

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
  title = entry_title.get()
  author = entry_author.get()

  if title == "" or author == "":
    label_result.config(text="제목과 저자를 모두 입력하세요.", fg="red")
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

#메인 윈도우
root = Tk()
root.title("도서 대출 관리 프로그램")
root.geometry("380x220")

Label(root, text="도서 대출 관리 시스템", font=("Arial", 13, "bold")).pack(pady=8)

#입력 영역
frame_input = Frame(root)
frame_input.pack(pady=5)

Label(frame_input, text="제목:").grid(row=0, column=0, padx=5, pady=5)
entry_title = Entry(frame_input, width=25)
entry_title.grid(row=0, column=1, padx=5, pady=5)

Label(frame_input, text="저자:").grid(row=1, column=0, padx=5, pady=5)
entry_author = Entry(frame_input, width=25)
entry_author.grid(row=1, column=1, padx=5, pady=5)

#버튼 영역
frame_btn = Frame(root)
frame_btn.pack(pady=10)

Button(frame_btn, text="대출", width=10, command=borrow_book).pack(side="left", padx=10)
Button(frame_btn, text="반납", width=10, command=return_book).pack(side="left", padx=10)

#결과 출력 라벨
label_result = Label(root, text="", font=("Arial", 11))
label_result.pack(pady=8)

root.mainloop()