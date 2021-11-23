import re

number_of_messages = int(input())
attacked_planets = []
destroyed_planets = []

for message in range(number_of_messages):
    encrypted_message = input()
    decrypted_message = ''

    pattern = r'[starSTAR]'
    matches = len(re.findall(pattern, encrypted_message))

    for character in encrypted_message:
        decrypted_character = chr((ord(character)) - matches)
        decrypted_message += decrypted_character

    planets_pattern = r'.*@(?P<planet>[A-Z][a-z]+)[^\@\-\!\:\>]*:(?P<population>\d+)[^\@\-\!\:\>]*\!(?P<attack_type>A|D)\![^\@\-\!\:\>]*\->(?P<soldiers>\d+).*'
    planet_matches = re.finditer(planets_pattern, decrypted_message)

    for value in planet_matches:
        planet, attack_type = value.group('planet'), value.group('attack_type')

        if attack_type == 'A':
            attacked_planets.append(planet)
        else:
            destroyed_planets.append(planet)

print(f'Attacked planets: {len(attacked_planets)}')
for planet in sorted(attacked_planets):
    print(f'-> {planet}')

print(f'Destroyed planets: {len(destroyed_planets)}')
for planet in sorted(destroyed_planets):
    print(f'-> {planet}')

