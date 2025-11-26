import os
base_dir = os.path.dirname(__file__)

infilename = os.path.join(base_dir, input("입력 파일 이름 : "))
outfilename = os.path.join(base_dir, input("출력 파일 이름 : "))

sum = 0
count = 0

with open(infilename, "r", encoding="utf-8") as infile, open(outfilename, "r", encoding="utf-8") as outfile:
    for line in infile:
        daliySale = int(line)
        sum += daliySale
        count += 1

    outfile.write("총매출 = " + str(sum) + "\n")
    outfile.write("평균 일매출 = " + str(sum // count))