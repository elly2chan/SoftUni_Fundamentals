courses = {}

while True:
    info = input()

    if info == 'end':
        break

    course_name, student_name = info.split(' : ')

    if course_name not in courses:
        courses[course_name] = []
    courses[course_name].append(student_name)

sorted_courses = sorted(courses.items(), key=lambda pair: len(pair[1]), reverse=True)
for course_name, students in sorted_courses:
    print(f'{course_name}: {len(students)}')
    for student in sorted(students):
        print(f'-- {student}')