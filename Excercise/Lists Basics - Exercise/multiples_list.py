factor = int(input())
count = int(input())
added_value = factor
result = []

for x in range(count):
    result.append(factor)
    factor += added_value

print(result)

# for x in range(1, count + 1):
#     result.append(factor * count)