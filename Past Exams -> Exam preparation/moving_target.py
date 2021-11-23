def shoot(targets, index, power):
    if index in range(len(targets)):
        if targets[index] > power:
            targets[index] -= power
        else:
            del targets[index]


def add(targets, index, value):
    if index in range(len(targets)):
        targets.insert(index, value)
    else:
        print('Invalid placement!')


def strike(targets, index, radius):
    start_index = index - radius
    end_index = index + radius

    if start_index in range(len(targets)) and end_index in range(len(targets)):
        targets = targets[0:start_index] + targets[end_index + 1:]
    else:
        print('Strike missed!')

    return targets


sequence_of_targets = [int(target) for target in input().split()]

while True:
    command = input()

    if command == 'End':
        break

    command = command.split()

    if command[0] == 'Shoot':
        index = int(command[1])
        power = int(command[2])
        shoot(sequence_of_targets, index, power)

    elif command[0] == 'Add':
        index = int(command[1])
        value = int(command[2])
        add(sequence_of_targets, index, value)

    elif command[0] == 'Strike':
        index = int(command[1])
        radius = int(command[2])
        sequence_of_targets = strike(sequence_of_targets, index, radius)

print('|'.join(str(target) for target in sequence_of_targets))
