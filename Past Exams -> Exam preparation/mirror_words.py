import re

data = input()

pattern = r'(@|#)([A-Za-z]{3,})(\1{2})([A-Za-z]{3,})(\1)'
hidden_words = re.findall(pattern, data)
mirror_words = []

for word in hidden_words:
    if word[1] == word[3][::-1]:
        mirror_words.append([word[1], word[3]])

result = ''

if hidden_words:
    print(f'{len(hidden_words)} word pairs found!')
else:
    print('No word pairs found!')

if mirror_words:
    print('The mirror words are:')
    for pair in mirror_words:
        result += pair[0] + ' <=> ' + pair[1] + ', '
    print(result[0:-1 - 1])
else:
    print('No mirror words!')
