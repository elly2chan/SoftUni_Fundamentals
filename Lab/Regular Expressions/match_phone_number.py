import re

phone_numbers = input()
pattern = r'\+359( |-)2(\1)\d{3}(\1)\d{4}\b'
matches = re.finditer(pattern, phone_numbers)

result = ''

for match in matches:
    match_str = match.group(0)
    result += match_str + ', '

print(result.rstrip(', '))
