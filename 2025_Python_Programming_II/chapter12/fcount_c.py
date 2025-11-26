import os
base_dir = os.path.dirname(__file__)
filename = input("파일명을 입력하세요 : ").strip()
filepath = os.path.join(base_dir, filename)

infile = open(filepath, "r", encoding="utf-8")

freqs = {}

for line in infile:
    for char in line.strip():
        if char in freqs:
            freqs[char] += 1
        else:
            freqs[char] = 1

print(freqs)
infile.close()