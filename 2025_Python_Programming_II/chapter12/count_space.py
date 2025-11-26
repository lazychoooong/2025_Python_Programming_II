import os

def parse_file(path):
    infile = open(path)

    spaces = 0
    tabs = 0

    for line in infile:
        spaces += line.count(" ")
        tabs += line.count("\t")

    infile.close()

    return spaces, tabs

base_dir = os.path.dirname(__file__)

filename = input("파일 이름을 입력하시오 : ")

filepath = os.path.join(base_dir, filename)

spaces, tabs = parse_file(filepath)
print(f"스페이스 수 = {spaces}, 탭의 수 = {tabs}")