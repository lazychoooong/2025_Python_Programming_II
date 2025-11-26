infile = open("2025_Python_Programming_II/chapter12/phones.txt", "r", encoding="utf-8") # 경로 설정 필요 / utf-8 인코딩 하면 한 칸씩 띄워짐
line = infile.readline()
while line != "":
    print(line)
    line = infile.readline()
infile.close()