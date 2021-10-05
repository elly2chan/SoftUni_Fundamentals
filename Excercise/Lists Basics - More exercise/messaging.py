string_of_numbers = input()
message = input()

list_of_numbers = string_of_numbers.split(' ')
current_index = 0
decoded_message = ''

for number in list_of_numbers:
    for digit in number:
        current_index += int(digit)
    length = len(message)
    if current_index > length:
        current_index = current_index - length
    decoded_message = decoded_message + message[current_index]
    message = message[0:current_index] + message[current_index + 1::]
    current_index = 0

print(decoded_message)

