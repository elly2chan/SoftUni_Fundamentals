given_year = int(input())

while True:
    given_year += 1
    if len(set(str(given_year))) == len(str(given_year)):
        break

print(given_year)
