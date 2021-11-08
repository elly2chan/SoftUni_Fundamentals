command = input()
courses = {}

while ':' in command:
    command = command.split(':')
    student = command[0]
    student_id = int(command[1])
    course = command[2]

    if course not in courses:
        courses[course] = {}

    courses[course][student] = student_id

    command = input()

searched_course = command.replace('_', ' ')
print(courses)
for student, student_id in courses[searched_course].items():
    print(f'{student} - {student_id}')