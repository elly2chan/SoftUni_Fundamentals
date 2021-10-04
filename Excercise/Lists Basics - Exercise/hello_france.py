items_with_prices = input()
budget = float(input())
items_with_prices = items_with_prices.split('|')
items_with_new_prices = []
money_spent = 0
profit = 0

for item in items_with_prices:
    current_item = item.split('->')
    item_type = current_item[0]
    item_price = float(current_item[1])

    if budget - item_price < 0:
        pass
    else:

        if item_type == 'Clothes':
            if item_price <= 50:
                budget -= item_price
                money_spent += item_price
                new_price = item_price + item_price * 0.4
                items_with_new_prices.append(new_price)

        if item_type == 'Shoes':
            if item_price <= 35:
                budget -= item_price
                money_spent += item_price
                new_price = item_price + item_price * 0.4
                items_with_new_prices.append(new_price)

        if item_type == 'Accessories':
            if item_price <= 20.50:
                budget -= item_price
                money_spent += item_price
                new_price = item_price + item_price * 0.4
                items_with_new_prices.append(new_price)


for priced_item in items_with_new_prices:
    print(f'{priced_item:.2f}', end=' ')
    profit += priced_item

print()
print(f'Profit: {(profit - money_spent):.2f}')

if budget + profit >= 150:
    print('Hello, France!')
else:
    print('Not enough money.')