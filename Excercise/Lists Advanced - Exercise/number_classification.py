sequence_of_numbers = input().split(', ')
sequence_of_numbers = [int(n) for n in sequence_of_numbers]


def positive_numbers(numbers):
    return [str(number) for number in numbers if number >= 0]


def negative_numbers(numbers):
    return [str(number) for number in numbers if number < 0]


def even_numbers(numbers):
    return [str(number) for number in numbers if number % 2 == 0]


def odd_numbers(numbers):
    return [str(number) for number in numbers if number % 2 != 0]


print(f"Positive: {', '.join(positive_numbers(sequence_of_numbers))}")
print(f"Negative: {', '.join(negative_numbers(sequence_of_numbers))}")
print(f"Even: {', '.join(even_numbers(sequence_of_numbers))}")
print(f"Odd: {', '.join(odd_numbers(sequence_of_numbers))}")
