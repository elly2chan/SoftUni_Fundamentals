message = input()

while True:
    command = input()

    if command == 'Decode':
        break

    command = command.split('|')

    if command[0] == 'Move':
        number_of_letters = int(command[1])
        characters_to_move = message[0:number_of_letters]
        message = message.replace(characters_to_move, '') + characters_to_move

    elif command[0] == 'Insert':
        index = int(command[1])
        value = command[2]
        message = message[0:index] + value + message[index:]

    elif command[0] == 'ChangeAll':
        substring = command[1]
        replacement = command[2]
        message = message.replace(substring, replacement)

print(f'The decrypted message is: {message}')