'''
도서관리 프로그램-v2

- 도서관리 프로그램-v1프로그램을 개선하세요.

1. 데이터 구조 추가
- 현재 대출 중인 도서 목록을 전역 리스트로 관리한다.
- borrowed_books: list[Book] = []

2. 화면(라벨) 구성 변경
- 대출 현황 라벨을 추가하여, 현재 대출 중인 도서의 목록을 표시한다.

3. 이벤트 핸들러 확장
- update_borrowed_list() 함수를 작성하여, borrowed_books 내용을 대출 현황 라벨에 반영한다.
- 대출/반납 처리 후 반드시 호출하여 화면을 갱신한다.

4. 대출 로직 강화
- [검증] 제목 또는 저자가 비어 있으면 오류 메시지(빨간색) 출력.
- [중복 방지] 동일 제목+저자 조합이 이미 대출 목록에 있으면
『제목』은(는) 이미 대출 중입니다. 메시지를 빨간색으로 출력하고 추가 대출 금지.
- [처리] 새 Book 객체를 만들고 borrow() 호출 후 borrowed_books에 추가. 결과 메시지는 파란색으로 출력.

5. 반납 로직 강화
- 제목 또는 저자가 비어 있으면 오류 메시지(빨간색) 출력.
- [처리] borrowed_books에서 제목+저자가 일치하는 도서를 찾아 제거하고,
『제목』이(가) 반납되었습니다.를 초록색으로 출력.
없으면 『제목』은(는) 대출 목록에 없습니다.를 빨간색으로 출력.

6. 창/레이아웃 조정
- 창 크기를 v2에 맞게 조정한다. (예: root.geometry("430x280"))
'''

#도서관리 프로그램_v2
from tkinter import *

#Book 클래스 정의
class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author
    self.borrowed = False

  def borrow(self):
    if not self.borrowed:
      self.borrowed = True
      return f"{self.title}이(가) 대출되었습니다."
    return f"{self.title}은(는) 이미 대출 중입니다."

  def return_book(self):
    if self.borrowed:
      self.borrowed = False
      return f"{self.title}이(가) 반납되었습니다."
    return f"{self.title}은(는) 대출되지 않은 상태입니다."

#현재 대출 중인 도서 리스트
borrowed_books = []  

#이벤트 핸들러
def update_borrowed_list():
  if borrowed_books:
    books_str = ", ".join([f"{b.title}({b.author})" for b in borrowed_books])
  else:
    books_str = "현재 대출 중인 도서가 없습니다."
  label_list.config(text=f"대출 현황: {books_str}")

def borrow_book():
  title = entry_title.get().strip()
  author = entry_author.get().strip()
  if not title or not author:
    label_result.config(text="제목과 저자를 모두 입력하세요.", fg="red")
    return

  #중복 대출 방지(제목+저자 기준)
  for b in borrowed_books:
    if b.title == title and b.author == author:
      label_result.config(text=f"{title}은(는) 이미 대출 중입니다.", fg="red")
      return

  book = Book(title, author)
  msg = book.borrow()  # 상태 True로 전환
  borrowed_books.append(book)
  label_result.config(text=msg, fg="blue")
  update_borrowed_list()

def return_book():
  title = entry_title.get().strip()
  author = entry_author.get().strip()
  if not title or not author:
    label_result.config(text="제목과 저자를 모두 입력하세요.", fg="red")
    return

  for b in borrowed_books:
    if b.title == title and b.author == author:
      borrowed_books.remove(b)
      label_result.config(text=f"{title}이(가) 반납되었습니다.", fg="green")
      update_borrowed_list()
      return

  label_result.config(text=f"{title}은(는) 대출 목록에 없습니다.", fg="red")

#GUI
root = Tk()
root.title("도서 대출 관리 프로그램")
root.geometry("430x280")

Label(root, text="도서 대출 관리 시스템", font=("Arial", 13, "bold")).pack(pady=8)

#입력 영역
frame_input = Frame(root)
frame_input.pack(pady=5)

Label(frame_input, text="제목:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_title = Entry(frame_input, width=30)
entry_title.grid(row=0, column=1, padx=5, pady=5)

Label(frame_input, text="저자:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_author = Entry(frame_input, width=30)
entry_author.grid(row=1, column=1, padx=5, pady=5)

#버튼 영역
frame_btn = Frame(root)
frame_btn.pack(pady=10)
Button(frame_btn, text="대출", width=12, command=borrow_book).pack(side="left", padx=10)
Button(frame_btn, text="반납", width=12, command=return_book).pack(side="left", padx=10)

#결과 및 현황
label_result = Label(root, text="", font=("Arial", 11))
label_result.pack(pady=5)

label_list = Label(root, text="대출 현황: 현재 대출 중인 도서가 없습니다.", wraplength=400, justify="left")
label_list.pack(pady=10)

root.mainloop()