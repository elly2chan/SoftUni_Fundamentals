string_of_numbers = input()
list_of_numbers = [int(n) for n in string_of_numbers.split(' ')]

if len(list_of_numbers) % 2 == 0:
    half = len(list_of_numbers) // 2
    first_half = list_of_numbers[0:half - 1]
    second_half = list_of_numbers[half + 1:]
    second_half.reverse()
else:
    half = len(list_of_numbers) // 2
    first_half = list_of_numbers[0:half]
    second_half = list_of_numbers[half + 1::]
    second_half.reverse()

first_player_result = 0
second_player_result = 0

for number in first_half:
    if number != 0:
        first_player_result += number
    else:
        first_player_result -= first_player_result * 0.2

for num in second_half:
    if num != 0:
        second_player_result += num
    else:
        second_player_result -= second_player_result * 0.2

if first_player_result < second_player_result:
    print(f'The winner is left with total time: {first_player_result:.1f}.')
else:
    print(f'The winner is right with total time: {second_player_result:.1f}')

