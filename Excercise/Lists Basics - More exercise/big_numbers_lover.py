string_of_integers = input()
list_of_integers = sorted(string_of_integers.split())
list_of_integers.reverse()

result = ''.join(list_of_integers)

print(result)
