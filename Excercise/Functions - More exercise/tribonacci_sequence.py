def generate_tribonacci_sequence(length):
    result = [1, 1, 2, 4]

    while length >= 0:

        if length < 4:
            index = 0
            result = []
            for number in range(index, length):
                if index == 0:
                    result.append(1)
                else:
                    result.append(index)
                index += 1
            break

        if length == 4:
            break

        index = len(result) - 1
        next_number = result[index] + result[index - 1] + result[index - 2]
        result.append(next_number)
        length -= 1

    return result


length_of_tribonacci_sequence = int(input())
tribonacci_sequence = generate_tribonacci_sequence(length_of_tribonacci_sequence)

output = ' '.join(map(str, tribonacci_sequence))
print(output)

