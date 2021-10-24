list_of_phones = [phone for phone in input().split(', ')]
command = input()

while command != 'End':
    command = command.split(' - ')

    if command[0] == 'Add':
        new_phone = command[1]
        if new_phone not in list_of_phones:
            list_of_phones.append(new_phone)

    elif command[0] == 'Remove':
        removed_phone = command[1]
        if removed_phone in list_of_phones:
            list_of_phones.remove(removed_phone)

    elif command[0] == 'Bonus phone':
        phones = command[1].split(':')
        old_phone = phones[0]
        new_phone = phones[1]

        if old_phone in list_of_phones:
            index = list_of_phones.index(old_phone) + 1
            list_of_phones.insert(index, new_phone)

    elif command[0] == 'Last':
        phone = command[1]
        if phone in list_of_phones:
            list_of_phones.remove(phone)
            list_of_phones.append(phone)

    command = input()

print(', '.join(list_of_phones))