number_of_lines = int(input())
result = []
filtered = []

for line in range(number_of_lines):
    number = int(input())
    result.append(number)

command = input()

for x in result:
    if command == "even":
        if x % 2 == 0:
            filtered.append(x)
    elif command == "odd":
        if x % 2 != 0:
            filtered.append(x)
    elif command == "negative":
        if x < 0:
            filtered.append(x)
    elif command == "positive":
        if x >= 0:
            filtered.append(x)

print(filtered)