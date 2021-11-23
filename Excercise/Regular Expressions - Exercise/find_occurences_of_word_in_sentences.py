import re

data = input().lower()
word = input().lower()

pattern = rf'\b{word}\b'
matches = re.findall(pattern, data)

print(len(matches))