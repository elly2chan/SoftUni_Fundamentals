result = ['0'] * 9

while True:
    command = input()

    if command == 'End':
        break
    command = command.split('-')
    priority = int(command[0]) - 1
    note = command[1]
    if result[priority] == '0':
        result[priority] = note

notes = [value for value in result if value != '0']
print(notes)