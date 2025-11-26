import os

base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, "phones.txt")
infile = open(file_path, "r", encoding="utf-8")
s = infile.read()
print(s)
infile.close()

print(base_dir)
print(file_path)