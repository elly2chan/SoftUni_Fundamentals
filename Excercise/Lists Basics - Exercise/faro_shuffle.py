string_of_cards = input()
count_of_faro_shuffles = int(input())
list_of_cards = string_of_cards.split(' ')
half = len(list_of_cards) // 2

for shuffle in range(count_of_faro_shuffles):
    result = []
    for card in range(half):
        result.append(list_of_cards[card])
        result.append(list_of_cards[half])
        half += 1
    list_of_cards = result
    half = len(list_of_cards) // 2

print(list_of_cards)


#[1, 2, 3, 4, 5, 6]

#[2, 3] [4, 5]
#[4, 2] [5, 3]

#[1, 4, 2, 5, 3, 6]

