import re

matches = []

while True:
    data = input()

    if len(data) == 0:
        break
    else:
        pattern = r'\d+'
        matches += re.findall(pattern, data)

print(' '.join(matches))
