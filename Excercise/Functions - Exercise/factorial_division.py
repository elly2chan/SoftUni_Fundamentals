def calculate_factorial(a, b):
    first_factorial = 1
    second_factorial = 1

    for x in range(2, a + 1):

        first_factorial *= x

    for y in range(2, b + 1):
        second_factorial *= y

    return first_factorial, second_factorial


first_number = int(input())
second_number = int(input())

first_result, second_result = calculate_factorial(first_number, second_number)
result = first_result / second_result

print(f'{result:.2f}')