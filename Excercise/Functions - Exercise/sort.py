def sort_list(sequence_of_integers):
    return sorted(sequence_of_integers)


string_of_integers = input()
list_of_integers = [int(integer) for integer in string_of_integers.split(' ')]

print(sort_list(list_of_integers))
