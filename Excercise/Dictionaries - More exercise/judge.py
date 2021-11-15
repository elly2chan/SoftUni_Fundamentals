submissions = {}
individual_standings = {}

while True:

    data = input()

    if data == 'no more time':
        break

    username, contest, points = data.split(' -> ')
    points = int(points)

    if contest in submissions:
        if username not in submissions[contest]:
            submissions[contest][username] = points
        else:
            if submissions[contest][username] < points:
                submissions[contest][username] = points
    else:
        submissions[contest] = {}
        submissions[contest][username] = points

    if username not in individual_standings:
        individual_standings[username] = {}
        individual_standings[username][contest] = points
    else:
        if contest in individual_standings[username]:
            if individual_standings[username][contest] < points:
                individual_standings[username][contest] = points
        else:
            individual_standings[username][contest] = points

for contest, users in submissions.items():
    print(f'{contest}: {len(users)} participants')
    counter = 1
    for user, points in sorted(users.items(), key=lambda user: (-user[1], user[0])):
        print(f'{counter}. {user} <::> {points}')
        counter += 1

total_scores = {}
for user, submissions in individual_standings.items():
    if user not in total_scores:
        total_scores[user] = 0
        for submission in submissions.values():
            total_scores[user] += submission

print('Individual standings:')
counter = 1
for user, total_points in sorted(total_scores.items(), key=lambda score: (-score[1], score[0])):
    print(f'{counter}. {user} -> {total_points}')
    counter += 1