text_input = input().replace(' ', '')
result = {}

for char in text_input:
    if char not in result:
        result[char] = 0
    result[char] += 1

for key, value in result.items():
    print(f'{key} -> {value}')