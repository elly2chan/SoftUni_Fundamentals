number_of_heroes = int(input())
heroes = {}

for hero in range(number_of_heroes):
    hero_name, hp, mp = input().split()
    if int(hp) <= 100 and int(mp) <= 200:
        heroes[hero_name] = [int(hp), int(mp)]

while True:
    command = input()

    if command == 'End':
        break

    command = command.split(' - ')
    action = command[0]

    if action == 'CastSpell':
        hero = command[1]
        mp_needed = int(command[2])
        spell_name = command[3]

        if heroes[hero][1] < mp_needed:
            print(f'{hero} does not have enough MP to cast {spell_name}!')
        else:
            heroes[hero][1] -= mp_needed
            print(f'{hero} has successfully cast {spell_name} and now has {heroes[hero][1]} MP!')

    elif action == 'TakeDamage':
        hero = command[1]
        damage = int(command[2])
        attacker = command[3]

        heroes[hero][0] -= damage

        if heroes[hero][0] > 0:
            print(f'{hero} was hit for {damage} HP by {attacker} and now has {heroes[hero][0]} HP left!')
        else:
            del heroes[hero]
            print(f'{hero} has been killed by {attacker}!')

    elif action == 'Recharge':
        hero = command[1]
        amount = int(command[2])

        if heroes[hero][1] + amount > 200:
            amount = 200 - heroes[hero][1]
            heroes[hero][1] += amount
        else:
            heroes[hero][1] += amount

        print(f'{hero} recharged for {amount} MP!')

    elif action == 'Heal':
        hero = command[1]
        amount = int(command[2])

        if heroes[hero][0] + amount > 100:
            amount = 100 - heroes[hero][0]
            heroes[hero][0] += amount
        else:
            heroes[hero][0] += amount

        print(f'{hero} healed for {amount} HP!')

ordered_heroes = sorted(heroes.items(), key=lambda data: (-data[1][0], data[0]))

for hero, stats in ordered_heroes:
    print(hero)
    print(f'  HP: {stats[0]}')
    print(f'  MP: {stats[1]}')