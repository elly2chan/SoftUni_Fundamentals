import re

data = input()

pattern = r'([#|\|])(?P<item>[A-Za-z\s]+)\1(?P<expiration>\d{2}\/\d{2}\/\d{2})\1(?P<calories>\d{1,5})\1'
matches = re.finditer(pattern, data)

items = []
total_calories = 0

for match in matches:
    item, expiration, calories = match.group('item'), match.group('expiration'), match.group('calories')
    items.append([item, expiration, calories])
    total_calories += int(calories)

print(f'You have food to last you for: {total_calories // 2000} days!')

for item in items:
    print(f'Item: {item[0]}, Best before: {item[1]}, Nutrition: {item[2]}')