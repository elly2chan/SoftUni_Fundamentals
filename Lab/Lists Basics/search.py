number = int(input())
word = input()
words = []

for n in range(number):
    new_word = input()
    words.append(new_word)

print(words)

for w in range(len(words) - 1, -1, -1):
    element = words[w]
    if word not in element:
        words.remove(element)

print(words)