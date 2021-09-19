quantity = int(input())
days = int(input())
counter = 0
cost = 0
spirit = 0

if days % 10 == 0:
    spirit -= 30

while counter < days:
    counter += 1
    if counter % 11 == 0:
        quantity += 2
    if counter % 2 == 0:
        cost += quantity * 2
        spirit += 5
        if counter % 3 == 0:
            cost += ((quantity * 5) + (quantity * 3))
            spirit += 13
        elif counter % 10 == 0:
            spirit -= 20
            cost += 23
    elif counter % 3 == 0:
        cost += ((quantity * 5) + (quantity * 3))
        spirit += 13
    elif counter % 5 == 0:
        cost += quantity * 15
        spirit += 17
        if counter % 5 == 0 and counter % 3 == 0:
            spirit += 30
    elif counter % 10 == 0:
        spirit -= 20
        cost += 23

print(f'Total cost: {cost}')
print(f'Total spirit: {spirit}')

