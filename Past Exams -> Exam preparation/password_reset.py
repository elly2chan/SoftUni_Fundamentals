def take_odd(password):
    new_password = ''
    for char_index in range(len(password)):
        if char_index % 2 != 0:
            new_password += password[char_index]
    return new_password


def cut(start_index, string_length, password):
    password = password.replace(password[start_index:start_index + string_length], '', 1)
    return password


def substitute(old_string, new_string, password):
    password = password.replace(old_string, new_string)
    return password


raw_password = input()

while True:
    command = input()

    if command == 'Done':
        break

    command = command.split()
    action = command[0]

    if action == 'TakeOdd':
        raw_password = take_odd(raw_password)
        print(raw_password)

    elif action == 'Cut':
        index = int(command[1])
        length = int(command[2])
        raw_password = cut(index, length, raw_password)
        print(raw_password)

    elif action == 'Substitute':
        substring = command[1]
        substitute_string = command[2]
        if substring in raw_password:
            raw_password = substitute(substring, substitute_string, raw_password)
            print(raw_password)
        else:
            print('Nothing to replace!')


print(f'Your password is: {raw_password}')