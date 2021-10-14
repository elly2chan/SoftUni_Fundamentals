string_input = input()
vowels = ['a', 'o', 'u', 'e', 'i', 'A', 'O', 'U', 'E', 'I']

result = ''.join([char for char in string_input if char not in vowels])

print(result)

