# Write a program that rounds all the given numbers, separated by a single space, and prints the result as a list.
# Use round()

sequence_of_numbers = input().split()
sequence_of_numbers = [float(x) for x in sequence_of_numbers]

result = map(lambda x: round(x), sequence_of_numbers)

print(list(result))