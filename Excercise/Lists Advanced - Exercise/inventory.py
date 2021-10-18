def collect_item(items, item):
    if item not in items:
        items.append(item)
    return items


def drop_item(items, item):
    if item in items:
        items.remove(item)
    return items


def combine_items(items, old_item, new_item):
    for index, item in enumerate(items):
        if item == old_item:
            items.insert(index + 1, new_item)
            break
    return items


def renew_item(items, to_be_renewed):
    for index, item in enumerate(items):
        if item == to_be_renewed:
            items.remove(item)
            items.append(item)
    return items


collecting_items = input().split(', ')
command = input()

while command != 'Craft!':
    command = command.split(' - ')

    if command[0] == 'Collect':
        item_to_collect = command[1]
        collecting_items = collect_item(collecting_items, item_to_collect)

    elif command[0] == 'Drop':
        item_to_drop = command[1]
        collecting_items = drop_item(collecting_items, item_to_drop)

    elif command[0] == 'Combine Items':
        items_to_combine = command[1].split(':')
        old = items_to_combine[0]
        new = items_to_combine[1]
        collecting_items = combine_items(collecting_items, old, new)

    elif command[0] == 'Renew':
        item_to_renew = command[1]
        collecting_items = renew_item(collecting_items, item_to_renew)

    command = input()

print(', '.join(collecting_items))