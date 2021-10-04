string_of_integers = input()
count_of_beggars = int(input())
list_of_integers = list(map(int, string_of_integers.split(', ')))
beggars_results = [0] * count_of_beggars
start = 0

for x in range(len(list_of_integers)):
    beggars_results[start] += list_of_integers[x]
    start += 1
    if start >= count_of_beggars:
        start = 0
print(beggars_results)