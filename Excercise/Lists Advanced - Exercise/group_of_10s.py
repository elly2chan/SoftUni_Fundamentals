string_of_numbers = input().split(', ')
list_of_numbers = [int(x) for x in string_of_numbers]
group_max = 10
counter = 0

while counter < len(list_of_numbers):
    current_group = []
    for number in list_of_numbers:
        if group_max - 10 < number <= group_max:
            current_group.append(number)
            counter += 1

    print(f"Group of {group_max}'s: {current_group}")
    group_max += 10