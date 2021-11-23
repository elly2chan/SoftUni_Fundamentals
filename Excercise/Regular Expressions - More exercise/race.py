import re

list_of_participants = input().split(', ')
racers = {}

while True:
    command = input()

    if command == 'end of race':
        break

    racer_pattern = r'[A-Za-z]'
    racer = re.findall(racer_pattern, command)
    distance_pattern = r'\d'
    distance = re.findall(distance_pattern, command)

    new_racer = ''
    racer_distance = 0

    for char in racer:
        new_racer += char

    for digit in distance:
        racer_distance += int(digit)

    if new_racer not in racers:
        racers[new_racer] = racer_distance
    else:
        racers[new_racer] += racer_distance

racers = {racer:distance for racer,distance in racers.items() if racer in list_of_participants}
sorted_racers = sorted(racers.items(), key=lambda pair: -pair[1])

print(f'1st place: {sorted_racers[0][0]}')
print(f'2nd place: {sorted_racers[1][0]}')
print(f'3rd place: {sorted_racers[2][0]}')