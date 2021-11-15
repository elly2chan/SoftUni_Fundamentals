number_of_dragons = int(input())
dragons = {}

for dragon in range(number_of_dragons):

    type, name, damage, health, armor = input().split(' ')

    if type not in dragons:
        dragons[type] = []
        dragons[type].append({name: [damage, health, armor]})