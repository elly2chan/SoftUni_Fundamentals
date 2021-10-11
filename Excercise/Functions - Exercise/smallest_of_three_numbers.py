first_number = int(input())
second_number = int(input())
third_number = int(input())


def smallest_of_three_numbers(a, b, c):
    return min(a, b, c)


print(smallest_of_three_numbers(first_number, second_number, third_number))