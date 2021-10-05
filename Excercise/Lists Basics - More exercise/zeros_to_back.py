integers_string = input()
integers_list = [int(n) for n in integers_string.split(', ')]

for integer in integers_list:
    if integer == 0:
        integers_list.remove(integer)
        integers_list.append(0)

print(integers_list)