rows_of_the_field = int(input())
field = []
ships_destroyed_count = 0

for row in range(rows_of_the_field):
    field_row = [int(position) for position in input().split(' ')]
    field.append(field_row)

squares_attacks = [square for square in input().split(' ')]

for square in squares_attacks:
    row_attacked = int(square[0])
    column_attacked = int(square[2])
    ship_attacked = field[row_attacked][column_attacked]
    if ship_attacked != 0:
        if ship_attacked == 1:
            field[row_attacked][column_attacked] -= 1
            ships_destroyed_count += 1
        else:
            field[row_attacked][column_attacked] -= 1

print(ships_destroyed_count)