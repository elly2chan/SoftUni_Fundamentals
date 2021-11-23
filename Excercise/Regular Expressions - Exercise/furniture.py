import re

furniture = []
total_price = 0

while True:
    data = input()

    if data == 'Purchase':
        break

    pattern = r'\b((?<=>>)[A-Za-z]+)(<<)(\d+\.?\d+)(!)(\d+)\b'
    matches = re.finditer(pattern, data)

    for match in matches:
        furniture_name = match.group(1)
        price = float(match.group(3))
        quantity = int(match.group(5))

        furniture.append(furniture_name)
        total_price += price * quantity

print('Bought furniture:')
for item in furniture:
    print(item)

print(f'Total money spend: {total_price:.2f}')