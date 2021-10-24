from math import floor

biscuits_per_day_per_worker = int(input())
count_of_workers = int(input())
competing_factory_biscuits_per_month = int(input())
total_biscuits_per_day = biscuits_per_day_per_worker * count_of_workers
days = 30
total = 0

for day in range(1, days + 1):
    total += total_biscuits_per_day

    if day % 3 == 0:
        total -= total_biscuits_per_day * 0.25
        total = floor(total)

print(f'You have produced {total} biscuits for the past month.')

if total > competing_factory_biscuits_per_month:
    difference = total - competing_factory_biscuits_per_month
    percentage = difference / competing_factory_biscuits_per_month * 100
    print(f'You produce {percentage:.2f} percent more biscuits.')
else:
    difference = competing_factory_biscuits_per_month - total
    percentage = difference / competing_factory_biscuits_per_month * 100
    print(f'You produce {percentage:.2f} percent less biscuits.')