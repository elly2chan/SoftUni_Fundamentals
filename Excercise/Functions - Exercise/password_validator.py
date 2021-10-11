from string import ascii_letters


def is_password_valid(password):
    conditions = 3
    is_not_char = 0
    has_digits = 0
    result = []

    if 6 <= len(password) <= 10:
        conditions -= 1
    else:
        result.append('Password must be between 6 and 10 characters')

    for char in password:
        if char not in ascii_letters:
            if not (48 <= ord(char) <= 57):
                is_not_char += 1
            else:
                has_digits += 1

    if is_not_char == 0:
        conditions -= 1
    else:
        result.append('Password must consist only of letters and digits')

    if has_digits >= 2:
        conditions -= 1
    else:
        result.append('Password must have at least 2 digits')

    if len(result) == 0:
        result.append('Password is valid')

    return result


password = input()

output = is_password_valid(password)

for value in output:
    print(value)