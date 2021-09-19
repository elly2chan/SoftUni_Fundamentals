divisor = int(input())
boundary = int(input())
largest_integer = 1

for number in range(1, boundary + 1):
    if number % divisor == 0 and number > largest_integer:
        largest_integer = number

print(largest_integer)