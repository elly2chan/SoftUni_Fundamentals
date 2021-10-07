input_product = input()
quantity_of_input_product = int(input())


def calculate_total_price(product, quantity_of_product):
    total = None
    if product == 'coffee':
        total = 1.50 * quantity_of_product
    elif product == 'water':
        total = 1.00 * quantity_of_product
    elif product == 'coke':
        total = 1.40 * quantity_of_product
    elif product == 'snacks':
        total = 2.00 * quantity_of_product

    return total


print(f'{(calculate_total_price(input_product, quantity_of_input_product)):.2f}')