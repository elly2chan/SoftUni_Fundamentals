usernames = [username for username in input().split(', ')]
command = input()
blacklisted = []
lost = []

while command != 'Report':
    command = command.split(' ')

    if command[0] == 'Blacklist':
        name = command[1]
        if name in usernames:
            index = usernames.index(name)
            blacklisted.append(name)
            usernames[index] = 'Blacklisted'
            print(f'{name} was blacklisted.')
        else:
            print(f'{name} was not found.')

    elif command[0] == 'Error':
        index = int(command[1])
        if index in range(len(usernames)) and index >= 0:
            name = usernames[index]
            if name != 'Blacklisted' and name != 'Lost':
                usernames[index] = 'Lost'
                lost.append(name)
                print(f'{name} was lost due to an error.')

    elif command[0] == 'Change':
        index = int(command[1])
        new_name = command[2]
        if index in range(len(usernames)) and index >= 0:
            current_name = usernames[index]
            usernames[index] = new_name
            print(f'{current_name} changed his username to {new_name}.')

    command = input()

print(f'Blacklisted names: {len(blacklisted)}')
print(f'Lost names: {len(lost)}')
print(' '.join(usernames))