command = input()
products_in_stock = {}

while command != 'statistics':
    command = command.split(': ')
    product = command[0]
    quantity = int(command[1])
    if product not in products_in_stock:
        products_in_stock[product] = quantity
    else:
        products_in_stock[product] += quantity

    command = input()

print('Products in stock:')
for (product, quantity) in products_in_stock.items():
    print(f'- {product}: {quantity}')
print(f'Total Products: {len(products_in_stock.keys())}')
print(f'Total Quantity: {sum(products_in_stock.values())}')