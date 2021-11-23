import re

dates = input()

pattern = r"(\d{2})(.|-|\/)([A-Z]{1}[a-z]{2})(\2)(\d{4})"
matches = re.finditer(pattern,dates)

for match in matches:
    day = match.group(1)
    month = match.group(3)
    year = match.group(5)

    print(f'Day: {day}, Month: {month}, Year: {year}')