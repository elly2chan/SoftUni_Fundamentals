data = input()
digits = ''
letters = ''
other_characters = ''

for ch in data:
    if ch.isnumeric():
        digits += ch
    elif ch.isalpha():
        letters += ch
    else:
        other_characters += ch

print(digits)
print(letters)
print(other_characters)