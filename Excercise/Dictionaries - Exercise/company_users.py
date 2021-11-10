companies = {}

while True:
    data = input()

    if data == 'End':
        break

    data = data.split(' -> ')
    company_name = data[0]
    employee_id = data[1]

    if company_name not in companies:
        companies[company_name] = []

    if employee_id not in companies[company_name]:
        companies[company_name].append(employee_id)

sorted_companies = sorted(companies.items())

for company, employees in sorted_companies:
    print(company)
    for employee in employees:
        print(f'-- {employee}')
