def calculate_cool_treshold(data):
    result = 1

    for word in data:
        for character in word:
            if character.isdigit():
                result *= int(character)

    return result


def find_valid_emojis(data):
    valid_emojis = []

    for word in data:
        if word[0] in (':', '*'):
            reversed_word = word[::-1]
            if (word[0] == word[1]) and (word[0] == reversed_word[0]) and (word[0] == reversed_word[1]):
                if word[2].isalpha() and word[2].isupper():
                    if len(word[2:-1 -1]) >= 3:
                        if word[3:-1 - 1].isalpha() and word[3:-1 -1].islower():
                            valid_emojis.append(word)

    return valid_emojis


def calculate_emojis_coolnes(emojis):
    cool_emojis = {}

    for emoji in emojis:
        emoji_coolness = 0
        for char in emoji:
            if char.isalpha():
                emoji_coolness += ord(char)
        cool_emojis[emoji] = emoji_coolness

    return cool_emojis


data = input().replace(',', '').replace('.', '').split()
cool_threshold = calculate_cool_treshold(data)
emojis = find_valid_emojis(data)
emojis_coolness = calculate_emojis_coolnes(emojis)

print(f'Cool threshold: {cool_threshold}')
print(f'{len(emojis)} emojis found in the text. The cool ones are:')
for emoji, coolness in emojis_coolness.items():
    if coolness >= cool_threshold:
        print(emoji)


