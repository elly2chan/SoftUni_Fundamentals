force_book = {}
is_found = False

while True:
    command = input()

    if command == 'Lumpawaroo':
        break

    if '|' in command:
        force_side, force_user = command.split(' | ')

        if force_side not in force_book:
            force_book[force_side] = []

        for value in force_book.values():
            if force_user in value:
                is_found = True

        if not is_found:
            force_book[force_side].append(force_user)

        is_found = False

    elif ' -> ' in command:
        force_user, force_side = command.split(' -> ')

        for value in force_book.values():
            if force_user in value:
                is_found = True
                value.remove(force_user)

        if force_side not in force_book:
            force_book[force_side] = []

        force_book[force_side].append(force_user)

        print(f'{force_user} joins the {force_side} side!')

sorted_force_book = sorted(force_book.items(), key=lambda side: (-len(side[1]), side[0]))

for side, users in sorted_force_book:
    if len(users) > 0:
        print(f'Side: {side}, Members: {len(users)}')
        for user in sorted(users):
            print(f'! {user}')