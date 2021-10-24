message = input()
result = ''
numbers_list = [str(number) for number in message if number.isdigit()]
string_list = [char for char in message if not char.isdigit()]

for index, number in enumerate(numbers_list):
    if index % 2 == 0:
        result += ''.join(string_list[:int(number)])
    string_list = string_list[int(number):]

print(result)
