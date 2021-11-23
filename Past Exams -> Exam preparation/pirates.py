cities = {}

while True:
    command = input()

    if command == 'Sail':
        break

    command = command.split('||')
    city = command[0]
    population = int(command[1])
    gold = int(command[2])

    if city in cities:
        cities[city][0] += population
        cities[city][1] += gold
    else:
        cities[city] = []
        cities[city].append(population)
        cities[city].append(gold)

while True:
    command = input()

    if command == 'End':
        break

    command = command.split('=>')
    action = command[0]

    if action == 'Plunder':
        town = command[1]
        people = int(command[2])
        gold = int(command[3])

        print(f'{town} plundered! {gold} gold stolen, {people} citizens killed.')

        cities[town][0] -= people
        cities[town][1] -= gold

        if cities[town][0] == 0 or cities[town][1] == 0:
            del cities[town]
            print(f'{town} has been wiped off the map!')

    elif action == 'Prosper':
        town = command[1]
        gold = int(command[2])

        if gold > 0:
            cities[town][1] += gold
            print(f'{gold} gold added to the city treasury. {town} now has {cities[town][1]} gold.')
        else:
            print('Gold added cannot be a negative number!')

sorted_cities = sorted(cities.items(), key=lambda city: (-city[1][1], city[0]))

if len(sorted_cities) > 0:
    print(f'Ahoy, Captain! There are {len(sorted_cities)} wealthy settlements to go to:')
    for city in sorted_cities:
        print(f'{city[0]} -> Population: {city[1][0]}, Gold: {city[1][1]} kg')
else:
    print('Ahoy, Captain! All targets have been plundered and destroyed!')

