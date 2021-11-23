targets = [int(target) for target in input().split()]

while True:
    command = input()

    if command == 'End':
        break

    target_index = int(command)

    if target_index in range(len(targets)):
        current_target = targets[target_index]
        targets[target_index] = -1

        for target in range(len(targets)):
            if targets[target] != -1:
                if targets[target] > current_target:
                    targets[target] -= current_target
                else:
                    targets[target] += current_target

print(f"Shot targets: {targets.count(-1)} -> {' '.join(str(target) for target in targets)}")