def read_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")

filename = input("텍스트 파일 이름을 입력하세요 : ")
read_file(filename)