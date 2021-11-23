sequence_of_elements = input().split()
moves_count = 0

while True:
    command = input()

    if command == 'end':
        break

    command = command.split()
    first_index = int(command[0])
    second_index = int(command[1])

    moves_count += 1

    if (first_index == second_index) or (first_index < 0) or (second_index < 0) or (first_index >= len(sequence_of_elements)) or (second_index >= len(sequence_of_elements)):
        index = len(sequence_of_elements) // 2
        sequence_of_elements.insert(index, f'-{moves_count}a')
        sequence_of_elements.insert(index, f'-{moves_count}a')
        print("Invalid input! Adding additional elements to the board")

    elif sequence_of_elements[first_index] == sequence_of_elements[second_index]:
        print(f'Congrats! You have found matching elements - {sequence_of_elements[first_index]}!')
        element = sequence_of_elements.pop(first_index)
        sequence_of_elements.remove(element)
    else:
        print("Try again!")

    if len(sequence_of_elements) == 0:
        print(f'You have won in {moves_count} turns!')
        break

if len(sequence_of_elements) > 0:
    print("Sorry you lose :(")
    print(' '.join(sequence_of_elements))