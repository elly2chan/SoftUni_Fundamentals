sequence_of_words = input().split(' ')
result = {}

for word in sequence_of_words:
    new_word = word.lower()
    if new_word not in result:
        result[new_word] = 0
    result[new_word] += 1

for key, value in result.items():
    if value % 2 != 0:
        print(key, end=' ')
