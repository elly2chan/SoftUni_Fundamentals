players_pool = {}

while True:

    command = input()

    if command == 'Season end':
        break

    if '->' in command:
        player, position, skill = command.split(' -> ')
        skill = int(skill)

        if player not in players_pool:
            players_pool[player] = {}
            players_pool[player][position] = skill
        else:
            if position in players_pool[player]:
                if skill > players_pool[player][position]:
                    players_pool[player][position] = skill
            else:
                players_pool[player][position] = skill

    # else:
    #     first_player, second_player = command.split(' vs ')
    #
    #     if (first_player, second_player) in players_pool:
    #

print(players_pool)
