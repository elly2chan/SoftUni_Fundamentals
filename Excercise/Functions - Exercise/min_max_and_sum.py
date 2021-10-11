def get_min_max_and_sum(integers):
    return min(integers), max(integers), sum(integers)


string_of_integers = input()
list_of_integers = [int(integer) for integer in string_of_integers.split(' ')]

min_integer, max_integer, sum_of_integers = get_min_max_and_sum(list_of_integers)
print(f'The minimum number is {min_integer}')
print(f'The maximum number is {max_integer}')
print(f'The sum number is: {sum_of_integers}')
