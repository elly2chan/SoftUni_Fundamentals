def sum_numbers(a, b):
    return a + b


def subtract(sum, number):
    return sum - number


def add_and_subtract(a, b, c):
    sum_of_first_two_integers = sum_numbers(first_number, second_number)
    subtract_numbers = subtract(sum_of_first_two_integers, third_number)
    return subtract_numbers


first_number = int(input())
second_number = int(input())
third_number = int(input())

print(add_and_subtract(first_number, second_number, third_number))

