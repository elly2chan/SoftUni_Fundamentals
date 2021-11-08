characters = input().split(', ')
result = {char: ord(char) for char in characters}

print(result)