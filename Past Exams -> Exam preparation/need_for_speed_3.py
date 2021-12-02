number_of_cars = int(input())
cars = {}

for number in range(number_of_cars):
    car, mileage, fuel = input().split('|')
    cars[car] = []
    cars[car].extend([int(mileage), int(fuel)])

while True:
    command = input()

    if command == 'Stop':
        break

    command = command.split(' : ')
    action = command[0]

    if action == 'Drive':
        current_car = command[1]
        distance = int(command[2])
        fuel_required = int(command[3])
        if cars[current_car][1] < fuel_required:
            print('Not enough fuel to make that ride')
        else:
            cars[current_car][0] += distance
            cars[current_car][1] -= fuel_required
            print(f'{current_car} driven for {distance} kilometers. {fuel_required} liters of fuel consumed.')
            if cars[current_car][0] >= 100_000:
                print(f'Time to sell the {current_car}!')
                del cars[current_car]

    elif action == 'Refuel':
        current_car = command[1]
        fuel_to_refill = int(command[2])
        tank_maximum = 75

        if cars[current_car][1] + fuel_to_refill > tank_maximum:
            fuel_to_refill = (tank_maximum - cars[current_car][1])
        cars[current_car][1] += fuel_to_refill
        print(f'{current_car} refueled with {fuel_to_refill} liters')

    elif action == 'Revert':
        current_car = command[1]
        kilometers = int(command[2])

        if cars[current_car][0] - kilometers >= 10_000:
            cars[current_car][0] -= kilometers
            print(f'{current_car} mileage decreased by {kilometers} kilometers')
        else:
            cars[current_car][0] = 10_000

sorted_cars = sorted(cars.items(), key=lambda data: (-data[1][0], data[0]))

for car, data in sorted_cars:
    print(f'{car} -> Mileage: {data[0]} kms, Fuel in the tank: {data[1]} lt.')