travel_stops = input()

while True:
    command = input()

    if command == 'Travel':
        break

    command = command.split(':')

    if command[0] == 'Add Stop':
        index = int(command[1])
        string = command[2]

        if index in range(len(travel_stops)):
            travel_stops = travel_stops[0:index] + string + travel_stops[index:]

    elif command[0] == 'Remove Stop':
        start_index = int(command[1])
        end_index = int(command[2])

        if start_index in range(len(travel_stops)) and end_index in range(len(travel_stops)):
            travel_stops = travel_stops[0:start_index] + travel_stops[end_index + 1:]

    elif command[0] == 'Switch':
        old_string = command[1]
        new_string = command[2]

        if old_string in travel_stops:
            travel_stops = travel_stops.replace(old_string, new_string)

    print(travel_stops)

print(f'Ready for world tour! Planned stops: {travel_stops}')