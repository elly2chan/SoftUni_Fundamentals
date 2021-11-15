data = input().split()
resulted_number = 0

for word in data:
    temp_number = ''
    for char in word:
        if char.isnumeric():
            temp_number += char
    temp_number = int(temp_number)

    letter_before = word[0].lower()
    letter_position = ((ord(letter_before) & 31))

    if word[0].isupper():
        temp_number /= letter_position
    else:
        temp_number *= letter_position

    resulted_number += temp_number

    letter_after = word[-1].lower()
    letter_position = ((ord(letter_after) & 31))

    if word[-1].isupper():
        resulted_number -= letter_position
    else:
        resulted_number += letter_position

print(f'{resulted_number:.2f}')

