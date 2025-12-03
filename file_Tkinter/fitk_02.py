def countWord(filename, search):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            count = content.count(search)
            return count
    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")
        return 0
    
filename = input("텍스트 파일 이름을 입력하세요 : ")
search = input("검색 문자열을 입력하세요 : ")

find = countWord(filename, search)
print(f"{search} (은)는 파일 내에서 {find}번 나타납니다.")