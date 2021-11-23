activation_key = input()

while True:
    command = input()

    if command == 'Generate':
        break

    command = command.split('>>>')
    action = command[0]

    if action == 'Contains':
        substring = command[1]
        if substring in activation_key:
            print(f'{activation_key} contains {substring}')
        else:
            print('Substring not found!')

    elif action == 'Flip':
        start_index = int(command[2])
        end_index = int(command[3])
        substring = ''

        for index in range(len(activation_key)):
            if index in range(start_index, end_index):
                substring += activation_key[index]

        if command[1] == 'Upper':
            activation_key = activation_key.replace(substring, substring.upper())
        elif command[1] == 'Lower':
            activation_key = activation_key.replace(substring, substring.lower())

        print(activation_key)

    elif action == 'Slice':
        start_index = int(command[1])
        end_index = int(command[2])
        substring = ''

        for index in range(len(activation_key)):
            if index in range(start_index, end_index):
                substring += activation_key[index]

        activation_key = activation_key.replace(substring, '')
        print(activation_key)

print(f'Your activation key is: {activation_key}')