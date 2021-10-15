current_version = input().split('.')
current_version = [int(x) for x in current_version]
current_version[-1] += 1

for current_index in range(len(current_version) - 1, -1, -1):
    if current_version[current_index] > 9:
        current_version[current_index] = 0
        if current_version[current_index - 1] >= 0:
            current_version[current_index - 1] += 1

print('.'.join(str(s) for s in current_version))

