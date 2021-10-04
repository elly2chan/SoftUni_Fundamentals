string_of_gifts = input()
command = input()
list_of_gifts = string_of_gifts.split(' ')

while command != "No Money":

    command = command.split(' ')
    gift = command[1]

    if command[0] == "OutOfStock":
        list_of_gifts = ["None" if gift in x else x for x in list_of_gifts]

    elif command[0] == "Required":
        index = int(command[2])
        if len(list_of_gifts) > index >= 0:
            list_of_gifts[index] = gift

    elif command[0] == "JustInCase":
        list_of_gifts[-1] = gift

    command = input()

while 'None' in list_of_gifts:
    list_of_gifts.remove('None')

for i in list_of_gifts:
    print(i, end=' ')