def add(collection, piece, composer, key):
    if piece in collection:
        print(f'{piece} is already in the collection!')
    else:
        collection[piece] = [composer, key]
        print(f'{piece} by {composer} in {key} added to the collection!')
    return collection


def remove(collection, piece):
    if piece in collection:
        print(f'Successfully removed {piece}!')
        collection.pop(piece)
    else:
        print(f'Invalid operation! {piece} does not exist in the collection.')
    return collection


def change_key(collection, piece, new_key):
    if piece in collection:
        collection[piece][1] = new_key
        print(f'Changed the key of {piece} to {new_key}!')
    else:
        print(f'Invalid operation! {piece} does not exist in the collection.')
    return collection


number_of_pieces = int(input())
collection = {}

for piece in range(number_of_pieces):
    title, composer, key = input().split('|')
    collection[title] = [composer, key]

while True:
    command = input()

    if command == 'Stop':
        break

    command = command.split('|')

    if command[0] == 'Add':
        piece, composer, key = command[1], command[2], command[3]
        add(collection, piece, composer, key)

    elif command[0] == 'Remove':
        piece = command[1]
        remove(collection, piece)

    elif command[0] == 'ChangeKey':
        piece, new_key = command[1], command[2]
        change_key(collection, piece, new_key)

sorted_collection = sorted(collection.items(), key=lambda pieces: (pieces[0], pieces[1][0]))

for piece in sorted_collection:
    print(f'{piece[0]} -> Composer: {piece[1][0]}, Key: {piece[1][1]}')
