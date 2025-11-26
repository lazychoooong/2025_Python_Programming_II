def caesar_cipher(text, key):
    result = ""
    for char in text:
        if char.isalpha():  # 알파벳인 경우에만 변환
            shift = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - shift + key) % 26 + shift)
            result += shifted_char
        else:
            result += char  # 알파벳이 아닌 경우 그대로 유지
    return result

def encrypt_file(input_file, output_file, key):
    with open(input_file, 'r') as file:
        plaintext = file.read()
    encrypted_text = caesar_cipher(plaintext, key)
    with open(output_file, 'w') as file:
        file.write(encrypted_text)

# 예시
input_filename = '2025_Python_Programming_II\\chapter12\\phones.txt'
encrypted_filename = '2025_Python_Programming_II\\chapter12\\phones(enc).txt'
encryption_key = 3
# 파일 암호화
encrypt_file(input_filename, encrypted_filename, encryption_key)
print(f"{input_filename}을(를) 암호화하여 {encrypted_filename}로 저장했습니다.")