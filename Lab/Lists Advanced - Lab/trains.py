def create_a_train(length):
    train = [0] * length
    command = input()

    while command != 'End':
        command = command.split()
        action = command[0]

        if action == 'add':
            people_count = int(command[1])
            train[-1] += people_count

        elif action == 'insert':
            index = int(command[1])
            people_count = int(command[2])
            train[index] += people_count

        elif action == 'leave':
            index = int(command[1])
            people_count = int(command[2])
            train[index] -= people_count

        command = input()

    return train


length_of_train = int(input())
print(create_a_train(length_of_train))
