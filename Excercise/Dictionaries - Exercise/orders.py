order = {}

while True:
    command = input()

    if command == 'buy':
        break

    command = command.split(' ')
    product = command[0]
    price = float(command[1])
    quantity = int(command[2])

    if product not in order:
        order[product] = {}
        order[product]['item_price'] = price
        order[product]['quantity'] = quantity
    else:
        order[product]['item_price'] = price
        order[product]['quantity'] += quantity

total_price = 1

for key, value in order.items():
    for v in value:
        total_price = total_price * value[v]
    print(f'{key} -> {total_price:.2f}')
    total_price = 1
