number_of_rooms = int(input())
counter = 0
chairs_left = 0
current_room = 0

for room in range(number_of_rooms):
    current_room += 1
    chairs_and_visitors = input().split(' ')
    chairs_in_room = chairs_and_visitors[0].count('X')
    visitors_count = int(chairs_and_visitors[1])
    if visitors_count > chairs_in_room:
        needed_chairs = visitors_count - chairs_in_room
        print(f'{needed_chairs} more chairs needed in room {current_room}')
    else:
        chairs_left += chairs_in_room - visitors_count
        counter += 1

if counter == number_of_rooms:
    print(f'Game On, {chairs_left} free chairs left')
