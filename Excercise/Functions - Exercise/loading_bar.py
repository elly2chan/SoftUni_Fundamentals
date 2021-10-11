def generate_a_loading_bar(integer):
    counter = integer // 10
    result = '%' * counter

    return result


percentage_completed = int(input())
output = generate_a_loading_bar(percentage_completed)

if len(output) == 10:
    print('100% Complete!')
    print(f'[{output}]')
else:
    dots = '.' * (10 - (percentage_completed // 10))
    print(f'{percentage_completed}% [{output}{dots}]')
    print('Still loading...')