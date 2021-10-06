from sys import maxsize

list_of_integers = input().split(' ')
list_of_integers = [int(x) for x in list_of_integers]
command = input()

while command != 'end':
    command = command.split(' ')

    #exchange command

    if command[0] == 'exchange':
        index = int(command[1])

        if index >= 0 and index in range(len(list_of_integers)):
            sublist_one = list_of_integers[0:index + 1]
            sublist_two = list_of_integers[index + 1:]
            list_of_integers = sublist_two + sublist_one
        else:
            print('Invalid index')

    #max even/odd command

    if command[0] == 'max':
        max_integer = -maxsize
        max_index = 0

        if command[1] == 'even':
            for index, integer in enumerate(list_of_integers):
                if integer % 2 == 0:
                    if integer > max_integer:
                        max_integer = integer
                        max_index = index
                    elif integer == max_integer:
                        max_integer = integer
                        max_index = index

        elif command[1] == 'odd':
            for index, integer in enumerate(list_of_integers):
                if integer % 2 != 0:
                    if integer > max_integer:
                        max_integer = integer
                        max_index = index
                    elif integer == max_integer:
                        max_integer = integer
                        max_index = index

        if max_integer == -maxsize:
            print('No matches')
        else:
            print(max_index)
    #min even/odd command

    if command[0] == 'min':
        min_integer = maxsize
        min_index = 0

        if command[1] == 'even':
            for index, integer in enumerate(list_of_integers):
                if integer % 2 == 0:
                    if integer < min_integer:
                        min_integer = integer
                        min_index = index
                    elif integer == min_integer:
                        min_integer = integer
                        min_index = index

        elif command[1] == 'odd':
            for index, integer in enumerate(list_of_integers):
                if integer % 2 != 0:
                    if integer < min_integer:
                        min_integer = integer
                        min_index = index
                    elif integer == min_integer:
                        min_integer = integer
                        min_index = index

        if min_integer == maxsize:
            print('No matches')
        else:
            print(min_index)

    #first count even/odd command

    if command[0] == 'first':
        count = int(command[1])
        counter = 0
        result = []

        if count > len(list_of_integers):
            print('Invalid count')
        else:

            if command[2] == 'even':
                for integer in list_of_integers:
                    if integer % 2 == 0:
                        result.append(integer)
                        counter += 1
                        if counter == count:
                            break
                        elif counter == len(list_of_integers):
                            break
            elif command[2] == 'odd':
                for integer in list_of_integers:
                    if integer % 2 != 0:
                        result.append(integer)
                        counter += 1
                        if counter == count:
                            break
                        elif counter == len(list_of_integers):
                            break
            print(result)

    #last count even/odd command

    if command[0] == 'last':
        reversed_list = list_of_integers[::-1]
        count = int(command[1])
        counter = 0
        result = []
        if count > len(reversed_list):
            print('Invalid count')
        else:

            if command[2] == 'even':
                for integer in reversed_list:
                    if integer % 2 == 0:
                        result.append(integer)
                        counter += 1
                        if counter == count:
                            break
                        elif counter == len(reversed_list):
                            break
            elif command[2] == 'odd':
                for integer in reversed_list:
                    if integer % 2 != 0:
                        result.append(integer)
                        counter += 1
                        if counter == count:
                            break
                        elif counter == len(reversed_list):
                            break
            print(result[::-1])

    command = input()

print(list_of_integers)