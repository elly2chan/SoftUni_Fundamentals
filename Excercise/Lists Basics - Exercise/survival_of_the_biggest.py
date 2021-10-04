string_of_integers = input()
count_of_smallest_values = int(input())
list_of_integers = list(map(int, string_of_integers.split(' ')))

for x in range(count_of_smallest_values):
    list_of_integers.remove(min(list_of_integers))

result = ', '.join(map(str, list_of_integers))
print(result)