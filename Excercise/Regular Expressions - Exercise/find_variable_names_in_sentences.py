import re

data = input()
pattern = r'\b_([A-Za-z0-9]+)\b'
matches = re.findall(pattern, data)

print(','.join(matches))