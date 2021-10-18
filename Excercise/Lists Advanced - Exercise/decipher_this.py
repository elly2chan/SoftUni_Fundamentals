# You are given a secret message you should decipher. To do that, you need to know that in each word:
#     • the second and the last letter are switched (e.g., Holle means Hello)
#     • the first letter is replaced by its character code (e.g., 72 means H)

# Input                | Output
# 72olle 103doo 100ya  | Hello good day

secret_message = input().split(' ')
result = []

for word in secret_message:
    ascii_part = ''
    char_part = ''
    for char in word:
        if char.isnumeric():
            ascii_part += char
        else:
            char_part += char

    if len(char_part) > 1:
        result.append((chr(int(ascii_part))) + char_part[-1] + char_part[1: - 1] + char_part[0])
    else:
        result.append((chr(int(ascii_part))) + char_part)

deciphered_message = ' '.join(result)
print(deciphered_message)



