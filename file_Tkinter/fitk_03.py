def merge_files(file1_path, file2_path, output_file_path):
    with open(file1_path, 'r', encoding='utf-8') as file1:
        file1_content = file1.read()

    with open(file2_path, 'r', encoding='utf-8') as file2:
        file2_content = file2.read()

    merged_content = file1_content + '\n' + file2_content

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(merged_content)

file1_path = 'file1.txt'
file2_path = 'file2.txt'
output_file_path = 'output.txt'

merge_files(file1_path, file2_path, output_file_path)        