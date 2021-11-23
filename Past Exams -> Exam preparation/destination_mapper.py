import re

world_places = input()

pattern = r'(=|\/)([A-Z][A-Za-z]{2,})\1'
matches = re.finditer(pattern, world_places)
destination = []
travel_points = 0

for match in matches:
    destination.append(match.group(2))
    travel_points += len(match.group(2))

print(f"Destinations: {', '.join(destination)}")
print(f'Travel Points: {travel_points}')
