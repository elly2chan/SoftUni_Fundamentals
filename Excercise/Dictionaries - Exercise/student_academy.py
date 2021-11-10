n = int(input())
students = {}

for _ in range(n):
    name = input()
    grade = float(input())

    if name not in students:
        students[name] = []
    students[name].append(grade)

filtered_grades = {}

for name, grades in students.items():
    average_grade = sum(grades) / len(grades)
    if average_grade >= 4.5:
        filtered_grades[name] = average_grade

sorted_grades = sorted(filtered_grades.items(), key=lambda student_grade: -student_grade[1])

for student, grade in sorted_grades:
    print(f'{student} -> {grade:.2f}')