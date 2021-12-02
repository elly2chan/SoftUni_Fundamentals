def urgent(item, items):
    if item not in items:
        items.insert(0, item)


def unnecessary(item, items):
    if item in items:
        items.remove(item)


def correct(old_item, new_item, items):
    if old_item in items:
        index = items.index(old_item)
        items[index] = new_item


def rearrange(item, items):
    if item in items:
        items.remove(item)
        items.append(item)


shopping_list = input().split('!')

while True:
    command = input()

    if command == 'Go Shopping!':
        break

    command = command.split()
    action = command[0]

    if action == 'Urgent':
        grocery = command[1]
        urgent(grocery, shopping_list)

    elif action == 'Unnecessary':
        grocery = command[1]
        unnecessary(grocery, shopping_list)

    elif action == 'Correct':
        old_grocery = command[1]
        new_grocery = command[2]
        correct(old_grocery, new_grocery, shopping_list)

    elif action == 'Rearrange':
        grocery = command[1]
        rearrange(grocery, shopping_list)

print(', '.join(shopping_list))