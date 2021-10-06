circle_of_people = input().split(' ')
current_kill = int(input())
executed = []
counter = 0

index = 0
while len(circle_of_people) > 0:
    counter += 1
    if counter % current_kill == 0:
        executed.append(circle_of_people.pop(index))
    else:
        index += 1

    if index >= len(circle_of_people):
        index = 0

result = ','.join(x for x in executed)

print(f'[{result}]')
