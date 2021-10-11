number_as_string = input()


def get_odd_and_even_numbers_sum(numbers):
    even_sum = 0
    odd_sum = 0

    for number in numbers:
        number = int(number)
        if number % 2 == 0:
            even_sum += number
        else:
            odd_sum += number

    return even_sum, odd_sum


even_sum, odd_sum = get_odd_and_even_numbers_sum(number_as_string)
print(f'Odd sum = {odd_sum}, Even sum = {even_sum}')