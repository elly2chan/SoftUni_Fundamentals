food_quantity = float(input()) * 1000
hay_quantity = float(input()) * 1000
cover_quantity = float(input()) * 1000
guinea_weight = float(input()) * 1000

counter = 1

while True:
    food_quantity -= 300

    if food_quantity < 0:
        break

    if counter % 2 == 0:
        given_hay = food_quantity * 0.05
        hay_quantity -= given_hay
        if hay_quantity < 0:
            break

    if counter % 3 == 0:
        cover_given = guinea_weight / 3
        cover_quantity -= cover_given
        if cover_quantity < 0:
            break

    if counter == 30:
        break

    counter += 1

if food_quantity > 0 and hay_quantity > 0 and cover_quantity > 0:
    print(f'Everything is fine! Puppy is happy! Food: {(food_quantity / 1000):.2f}, Hay: {(hay_quantity / 1000):.2f}, '
          f'Cover: {(cover_quantity / 1000):.2f}.')
else:
    print('Merry must go to the pet store!')