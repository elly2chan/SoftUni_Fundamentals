neighbourhood = [int(hearts) for hearts in input().split('@')]
position = 0

while True:
    command = input()

    if command == 'Love!':
        break

    command = command.split()
    jump_length = int(command[1])

    if position + jump_length in range(len(neighbourhood)):
        position += jump_length
        if neighbourhood[position] == 0:
            print(f"Place {position} already had Valentine's day.")
        else:
            neighbourhood[position] -= 2
            if neighbourhood[position] == 0:
                print(f"Place {position} has Valentine's day.")

    else:
        position = 0
        if neighbourhood[position] == 0:
            print(f"Place {position} already had Valentine's day.")
        else:
            neighbourhood[position] -= 2
            if neighbourhood[position] == 0:
                print(f"Place {position} has Valentine's day.")


print(f"Cupid's last position was {position}.")

if sum(neighbourhood) == 0:
    print('Mission was successful.')
else:
    counter = 0
    for house in neighbourhood:
        if house > 0:
            counter += 1
    print(f'Cupid has failed {counter} places.')