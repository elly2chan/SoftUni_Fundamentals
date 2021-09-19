budget = float(input())
flour_price_per_kg = float(input())
eggs_price_per_pack = flour_price_per_kg * 0.75
milk_liter_price = flour_price_per_kg + (flour_price_per_kg * 0.25)
milk_price_per_bread = milk_liter_price / 4

bread_counter = 0
colored_eggs = 0

while budget > 0:
    sum_of_prices = eggs_price_per_pack + flour_price_per_kg + milk_price_per_bread
    if budget - sum_of_prices < 0:
        break
    else:
        budget -= sum_of_prices
        colored_eggs += 3
        bread_counter += 1
        if bread_counter % 3 == 0:
            colored_eggs -= (bread_counter - 2)

print(f'"You made {bread_counter} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left."')