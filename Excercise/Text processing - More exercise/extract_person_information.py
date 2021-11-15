def extract_name(data):
    name = ''
    for word in data:
        if '@' in word and '|' in word:
            end_index = word.index('|')
            for index in range(end_index - 1, 0, -1):
                while word[index] != '@':
                    name += word[index]
                    index -= 1
                break

    return name[::-1]


def extract_age(data):
    age = ''
    for word in data:
        if '#' in word and '*' in word:
            end_index = word.index('*')
            for index in range(end_index - 1, 0, -1):
                while word[index] != '#':
                    age += word[index]
                    index -= 1
                break

    return age[::-1]


number_of_people = int(input())

for person in range(number_of_people):
    text = input().split()
    name, age = extract_name(text), extract_age(text)
    print(f'{name} is {age} years old.')


