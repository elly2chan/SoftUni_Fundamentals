data = input()
current_data = ''
result = ''
unique_symbols = []
for index in range(len(data)):
    if not data[index].isdigit():
        if data[index].upper() not in unique_symbols:
            unique_symbols.append(data[index].upper())
        current_data += data[index]
    else:
        digit = ''
        while index < len(data) and data[index].isdigit():
            digit += data[index]
            index += 1
        result += current_data.upper() * int(digit)
        current_data = ''
        digit = ''

print(f'Unique symbols used: {len(unique_symbols)}')
print(result)