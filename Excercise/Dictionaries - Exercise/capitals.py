countries = input().split(', ')
capitals = input().split(', ')

result = {country: capital for country, capital in zip(countries, capitals)}

for country, capital in result.items():
    print(f'{country} -> {capital}')