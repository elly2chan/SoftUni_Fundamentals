user_points = {}
language_submissions = {}

while True:
    command = input()

    if command == 'exam finished':
        break

    data = command.split('-')

    if data[1] == 'banned':
        username = data[0]
        del user_points[username]
    else:
        username, language, points = data
        points = int(points)

        if username not in user_points:
            user_points[username] = points
        else:
            if points > user_points[username]:
                user_points[username] = points

        if language not in language_submissions:
            language_submissions[language] = 0
        language_submissions[language] += 1

sorted_users = sorted(user_points.items(), key=lambda user: (-user[1], user[0]))
print('Results:')
for user, max_points in sorted_users:
    print(f'{user} | {max_points}')

sorted_submissions = sorted(language_submissions.items(), key=lambda submission: (-submission[1], submission[0]))
print('Submissions:')
for language, submissions in sorted_submissions:
    print(f'{language} - {submissions}')