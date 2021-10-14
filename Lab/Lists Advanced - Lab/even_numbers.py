string_of_numbers = input().split(', ')
string_of_numbers = [int(number) for number in string_of_numbers]
result = []

for index, value in enumerate(string_of_numbers):
    if value % 2 == 0:
        result.append(index)

print(result)