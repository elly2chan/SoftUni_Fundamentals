energy = int(input())
battles_won_count = 0
game_won = True

while True:
    command = input()

    if command == 'End of battle':
        break

    distance_to_enemy = int(command)

    if energy >= distance_to_enemy:
        energy -= distance_to_enemy
        battles_won_count += 1
    else:
        print(f'Not enough energy! Game ends with {battles_won_count} won battles and {energy} energy')
        game_won = False
        break

    if battles_won_count % 3 == 0:
        energy += battles_won_count

if game_won:
    print(f'Won battles: {battles_won_count}. Energy left: {energy}')

