first_char = input()
second_char = input()
text = input()

start = ord(first_char)
end = ord(second_char)

result = 0

for character in text:
    if start < ord(character) < end:
        result += ord(character)

print(result)