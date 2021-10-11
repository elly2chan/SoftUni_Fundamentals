first_character = input()
second_character = input()


def characters_in_between(char_one, char_two):
    result = []
    for char in range(ord(char_one) + 1, ord(char_two)):
        result.append(chr(char))

    return ' '.join(result)


print(characters_in_between(first_character, second_character))