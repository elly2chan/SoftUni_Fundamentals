first_round = input().split(' ')
second_round = input().split(' ')
third_round = input().split(' ')

winner = '0'

#sample input
# 2 0 1
# 0 1 0
# 1 0 2

while True:

#lines

    if first_round.count(first_round[0]) == len(first_round):
        winner = first_round[0]
    elif second_round.count(second_round[0]) == len(second_round):
        winner = second_round[0]
    elif third_round.count(third_round[0]) == len(third_round):
        winner = third_round[0]

    #columns

    counter = 0
    index = 0
    while counter < len(first_round):
        if first_round[index] == second_round[index] == third_round[index]:
            winner = first_round[index]
        index += 1
        counter += 1

    #diagonals

    diag_index = 0

    if first_round[diag_index] == second_round[diag_index + 1] == third_round[diag_index + 2]:
        winner = first_round[diag_index]
    elif first_round[diag_index + 2] == second_round[diag_index + 1] == third_round[diag_index]:
        winner = first_round[diag_index + 2]

    #check if there is a winner

    if winner in ('0', '1', '2'):
        break

if winner == '1':
    print('First player won')
elif winner == '2':
    print('Second player won')
else:
    print('Draw!')