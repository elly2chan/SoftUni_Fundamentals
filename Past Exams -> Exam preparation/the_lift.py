people_waiting = int(input())
lift_cabins = [int(n) for n in input().split()]
maximum_lift_capacity = len(lift_cabins) * 4

for cabin in range(len(lift_cabins)):
    if lift_cabins[cabin] == 4:
        cabin += 1
    else:
        while lift_cabins[cabin] < 4:
            if people_waiting == 0 or (maximum_lift_capacity == sum(lift_cabins)):
                break

            lift_cabins[cabin] += 1
            people_waiting -= 1

if people_waiting == 0 and maximum_lift_capacity > sum(lift_cabins):
    print("The lift has empty spots!")
if people_waiting > 0 and maximum_lift_capacity == sum(lift_cabins):
    print(f"There isn't enough space! {people_waiting} people in a queue!")

print(' '.join(str(cabin) for cabin in lift_cabins))