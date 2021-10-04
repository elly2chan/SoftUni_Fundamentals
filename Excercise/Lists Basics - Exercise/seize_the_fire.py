# High = 89#Low = 28#Medium = 77#Low = 23
# 1250

type_of_fire = input()
amount_of_water = int(input())
list_of_fires = type_of_fire.split('#')
effort = 0
cells_put_out = []
total_fire = 0

for fire in list_of_fires:
    current_fire = fire.split(' ')
    degree = current_fire[0]
    value_of_cell = int(current_fire[2])
    effort_value = value_of_cell * 0.25
    if amount_of_water - value_of_cell < 0:
        pass
    else:
        if degree == 'High':
            if value_of_cell in range(81, 126):
                amount_of_water -= value_of_cell
                cells_put_out.append(value_of_cell)
                effort += effort_value
                total_fire += value_of_cell
        elif degree == 'Medium':
            if value_of_cell in range(51, 81):
                amount_of_water -= value_of_cell
                cells_put_out.append(value_of_cell)
                effort += effort_value
                total_fire += value_of_cell
        elif degree == 'Low':
            if value_of_cell in range(1, 51):
                amount_of_water -= value_of_cell
                cells_put_out.append(value_of_cell)
                effort += effort_value
                total_fire += value_of_cell



print('Cells:')
for cell in cells_put_out:
    print(f'- {cell}')
print(f'Effort: {effort:.2f}')
print(f'Total fire: {total_fire}')