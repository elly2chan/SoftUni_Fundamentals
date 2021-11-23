import re

total_income = 0

while True:
    data = input()

    if data == 'end of shift':
        break

    pattern = r"\%(?P<username>[A-Z][a-z]+)\%[^\|\$\%\.]*?\<(?P<product>\w+)\>[^\|\$\%\.]*?\|(?P<count>[\d+]+)\|[\w\-]*?(?P<price>[\d.]+[\d+])\$$"
    matches = re.finditer(pattern, data)

    for match in matches:
        username, product, count, price = match.group('username'), match.group('product'), int(match.group('count')), float(match.group('price'))
        print(f'{username}: {product} - {(count * price):.2f}')
        total_income += count * price

print(f'Total income: {total_income:.2f}')