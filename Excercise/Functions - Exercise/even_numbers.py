sequence_of_integers = input()
sequence_of_integers = [int(integer) for integer in sequence_of_integers.split(' ')]

is_even = lambda x: x % 2 == 0
result = list(filter(is_even, sequence_of_integers))

print(result)
