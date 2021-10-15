number_of_electrons = int(input())
filled_shells = []
index = 1

while number_of_electrons > 0:
    shell_capacity = 2 * (index ** 2)
    if number_of_electrons >= shell_capacity:
        filled_shells.append(shell_capacity)
    else:
        filled_shells.append(number_of_electrons)

    number_of_electrons -= shell_capacity
    index += 1

print(filled_shells)
