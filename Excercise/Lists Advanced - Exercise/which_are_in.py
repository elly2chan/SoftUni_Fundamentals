first_sequence_of_words = input().split(', ')
second_sequence_of_words = input().split(', ')
result = []

for word in first_sequence_of_words:
    for string in second_sequence_of_words:
        if word in string and word not in result:
            result.append(word)

print(result)

