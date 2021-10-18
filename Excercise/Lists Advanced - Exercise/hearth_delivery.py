houses_in_neighbourhood = input().split('@')
houses_in_neighbourhood = [int(house) for house in houses_in_neighbourhood]
jump_command = input()
position = 0

while jump_command != 'Love!':
    jump_command = jump_command.split(' ')
    jump_length = int(jump_command[1])

    if position + jump_length in range(len(houses_in_neighbourhood)):
        position += jump_length
        if houses_in_neighbourhood[position] == 0:
            print(f"Place {position} already had Valentine's day.")
        else:
            houses_in_neighbourhood[position] -= 2
            if houses_in_neighbourhood[position] == 0:
                print(f"Place {position} has Valentine's day.")
    else:
        position = 0
        if houses_in_neighbourhood[position] == 0:
            print(f"Place {position} already had Valentine's day.")
        else:
            houses_in_neighbourhood[position] -= 2
            if houses_in_neighbourhood[position] == 0:
                print(f"Place {position} has Valentine's day.")

    jump_command = input()

print(f"Cupid's last position was {position}.")
if sum(houses_in_neighbourhood) == 0:
    print('Mission was successful.')
else:
    result = [x for x in houses_in_neighbourhood if x != 0]
    print(f'Cupid has failed {len(result)} places.')
