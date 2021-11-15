keys = [int(key) for key in input().split()]
result = ''

while True:
    text = input()

    if text == 'find':
        break

    for character in text:
        character = ord(character)
        for index in range(len(keys)):
            if index == len(keys):
                index = 0
            result += chr(character - int(keys[index]))

print(result)