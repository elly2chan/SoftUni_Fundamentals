contests = {}

while True:
    data = input()

    if data == 'end of contests':
        break

    data = data.split(':')
    contest = data[0]
    password = data[1]

    contests[contest] = password

submissions = {}

while True:
    user_submission = input()

    if user_submission == 'end of submissions':
        break

    user_submission = user_submission.split('=>')
    submitted_contest = user_submission[0]
    submitted_password = user_submission[1]
    username = user_submission[2]
    points = int(user_submission[3])

    if submitted_contest in contests:
        if submitted_password == contests[submitted_contest]:
            if username not in submissions:
                submissions[username] = {}
            if submitted_contest not in submissions[username]:
                submissions[username][submitted_contest] = points
            else:
                if submissions[username][submitted_contest] < points:
                    submissions[username][submitted_contest] = points

best_candidate = ''
max_points = 0

for user, courses in submissions.items():
    total_points = 0
    for course in courses.items():
        total_points += course[1]
    if total_points > max_points:
        max_points = total_points
        best_candidate = user

print(f'Best candidate is {best_candidate} with total {max_points} points.')
print('Ranking:')

sorted_submissions = sorted(submissions.items())

for user, courses in sorted_submissions:
    print(user)
    for course, points in sorted(courses.items(), key=lambda course: -course[1]):
        print(f'#  {course} -> {points}')


