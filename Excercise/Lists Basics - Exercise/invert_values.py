string_of_numbers = input()
list_of_numbers = map(int, string_of_numbers.split())
result = []

for x in list_of_numbers:
    if x == 0:
        result.append(x)
    elif x > 0:
        result.append(-abs(x))
    elif x < 0:
        result.append(abs(x))

print(result)