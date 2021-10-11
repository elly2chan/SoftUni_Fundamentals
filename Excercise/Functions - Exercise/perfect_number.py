def is_perfect(integer):
    divisors = []
    result = None

    for divisor in range(1, integer):
        if integer % divisor == 0:
            divisors.append(divisor)

    if sum(divisors) == integer:
        result = True
    else:
        result = False

    return result


number = int(input())
output = is_perfect(number)

if output:
    print('We have a perfect number!')
else:
    print("It's not so perfect")
