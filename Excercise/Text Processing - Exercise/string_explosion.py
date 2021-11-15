data = input()
strength = 0
result = ''

for index in range(len(data)):
    if data[index] != '>' and strength > 0:
        strength -= 1
    elif data[index] == '>':
        strength += int(data[index + 1])
        result += data[index]
    else:
        result += data[index]

print(result)