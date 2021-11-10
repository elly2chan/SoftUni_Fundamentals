number_of_commands = int(input())
parking_database = {}

for command in range(number_of_commands):
    action = input().split(' ')
    command_type = action[0]
    username = action[1]

    if command_type == 'register':
        licence_plate_number = action[2]
        if username not in parking_database:
            parking_database[username] = licence_plate_number
            print(f'{username} registered {licence_plate_number} successfully')
        else:
            print(f'ERROR: already registered with plate number {parking_database[username]}')

    elif command_type == 'unregister':
        if username in parking_database:
            del parking_database[username]
            print(f'{username} unregistered successfully')
        else:
            print(f'ERROR: user {username} not found')

for key, value in parking_database.items():
    print(f'{key} => {value}')