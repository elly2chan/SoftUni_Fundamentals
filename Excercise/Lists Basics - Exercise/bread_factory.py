working_day_events = input()
working_day_events = working_day_events.split('|')
energy = 100
coins = 100
is_open = True

for event in working_day_events:
    event_is = event.split('-')
    event_or_ingredient = event_is[0]
    value = int(event_is[1])

    if event_or_ingredient == 'rest':
        if energy + value <= 100:
            energy += value
            print(f'You gained {value} energy.')
        else:
            print(f'You gained 0 energy.')
        print(f'Current energy: {energy}.')

    elif event_or_ingredient == 'order':
        if energy >= 30:
            energy -= 30
            coins += value
            print(f'You earned {value} coins.')
        else:
            energy += 50
            print(f'You had to rest!')

    else:
        if coins > value:
            print(f'You bought {event_or_ingredient}.')
            coins -= value
        else:
            is_open = False
            print(f'Closed! Cannot afford {event_or_ingredient}.')
            break

if is_open:
    print('Day completed!')
    print(f'Coins: {coins}')
    print(f'Energy: {energy}')
