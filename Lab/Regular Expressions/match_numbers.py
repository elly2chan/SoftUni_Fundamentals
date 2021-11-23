import re

data = input()
pattern = r'(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))'
matches = re.finditer(pattern, data)

result = ''
for match in matches:
    result += match.group(0) + ' '

print(result.rstrip())