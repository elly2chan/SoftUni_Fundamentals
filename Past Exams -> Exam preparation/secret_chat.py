def insert_space(message, index):
    message = message[0:index] + ' ' + message[index:]
    print(message)
    return message


def reverse(message, substring):
    if substring in message:
        message = message.replace(substring, '', 1)
        message = message + substring[::-1]
        print(message)
    else:
        print('error')
    return message


def change_all(message, substring, replacement):
    if substring in message:
        message = message.replace(substring, replacement)
        print(message)
    return message


message = input()

while True:
    command = input()

    if command == 'Reveal':
        break

    command = command.split(':|:')

    if command[0] == 'InsertSpace':
        index = int(command[1])
        message = insert_space(message, index)

    elif command[0] == 'Reverse':
        substring = command[1]
        message = reverse(message, substring)

    elif command[0] == 'ChangeAll':
        substring = command[1]
        replacement = command[2]
        message = change_all(message, substring, replacement)


print(f'You have a new text message: {message}')