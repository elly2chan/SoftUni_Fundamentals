sequence_of_numbers = input().split()
sequence_of_numbers = [float(x) for x in sequence_of_numbers]

for index, number in enumerate(sequence_of_numbers):
    sequence_of_numbers[index] = abs(number)

print(sequence_of_numbers)