text = input()
ciphered_text = ''

for char in text:
    ciphered_text += chr(ord(char) + 3)

print(ciphered_text)