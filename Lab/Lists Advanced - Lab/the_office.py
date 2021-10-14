list_of_employees_happiness_rates = input()
list_of_employees_happiness_rates = [int(x) for x in list_of_employees_happiness_rates.split(' ')]
happiness_improvement_factor = int(input())
counter = 0

for index, employee in enumerate(list_of_employees_happiness_rates):
    list_of_employees_happiness_rates[index] = employee * 3

sum_of_happiness = sum(list_of_employees_happiness_rates)
average_happiness = sum_of_happiness / len(list_of_employees_happiness_rates)

for employee in list_of_employees_happiness_rates:
    if employee >= average_happiness:
        counter += 1

if counter >= (len(list_of_employees_happiness_rates) / 2):
    print(f'Score: {counter}/{len(list_of_employees_happiness_rates)}. Employees are happy!')
else:
    print(f'Score: {counter}/{len(list_of_employees_happiness_rates)}. Employees are not happy!')
