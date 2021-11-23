customer_type = ''
total_price_without_taxes = 0
total_amount_of_taxes = 0

while True:
    command = input()

    if command == 'special':
        customer_type = 'special'
        break
    elif command == 'regular':
        break

    price = float(command)

    if price < 0:
        print('Invalid price!')
    else:
        total_price_without_taxes += price
        total_amount_of_taxes += price * 0.2

total_price = total_price_without_taxes + total_amount_of_taxes

if total_price == 0:
    print('Invalid order!')
else:
    if customer_type == 'special':
        total_price -= total_price * 0.1

    print("Congratulations you've just bought a new computer!")
    print(f'Price without taxes: {total_price_without_taxes:.2f}$')
    print(f'Taxes: {total_amount_of_taxes:.2f}$')
    print('-----------')
    print(f'Total price: {total_price:.2f}$')
