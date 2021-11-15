def is_winning(ticket):
    if len(ticket) != 20:
        return 'invalid ticket'

    left_half = ticket[:10]
    right_half = ticket[10:]
    winning_characters = ['@', '#', '$', '^']

    for character in winning_characters:
        for repetition in range(10, 5, -1):
            character_repetition = character * repetition
            if character_repetition in left_half and character_repetition in right_half:
                if repetition == 10:
                    return f'ticket "{ticket}" - {len(character_repetition)}{character} Jackpot!'
                elif 6 <= repetition <= 9:
                    return f'ticket "{ticket}" - {len(character_repetition)}{character}'

    return f'ticket "{ticket}" - no match'


tickets = [ticket.strip() for ticket in input().split(', ')]
tickets_states = []

for ticket in tickets:
    tickets_states.append(is_winning(ticket))

for ticket in tickets_states:
    print(ticket)