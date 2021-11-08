result = {}
counter = 1
key = ''

while True:
    command = input()

    if command == 'stop':
        break

    if counter % 2 != 0:
        key = command
        if key not in result:
            result[key] = 0
    else:
        value = int(command)
        result[key] += value

    counter += 1

for key, value in result.items():
    print(f'{key} -> {value}')