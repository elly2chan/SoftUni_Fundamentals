import math


def calculate_line_length_between_two_points(a1, b1, a2, b2):
    if (a1 >= 0 and a2 >= 0) or (a1 <= 0 and a2 <= 0):
        a = abs(a1 - a2)
    else:
        a = abs(a1) + abs(a2)

    if (b1 >= 0 and b2 >= 0) or (b1 <= 0 and b2 <= 0):
        b = abs(b1 - b2)
    else:
        b = abs(b1) + abs(b2)
    return (a ** 2 + b ** 2) ** 0.5


def floor_number(x):
    if x.is_integer():
        num = int(x)
    else:
        num = math.floor(x)
    return num


def closest_point(a1, b1, a2, b2):
    first_radius = (a1 ** 2 + b1 ** 2) ** 0.5
    second_radius = (a2 ** 2 + b2 ** 2) ** 0.5
    if first_radius <= second_radius:
        print(f"({floor_number(a1)}, {floor_number(b1)})({floor_number(a2)}, {floor_number(b2)})")
    else:
        print(f"({floor_number(a2)}, {floor_number(b2)})({floor_number(a1)}, {floor_number(b1)})")


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

a1 = float(input())
b1 = float(input())
a2 = float(input())
b2 = float(input())

first_line = calculate_line_length_between_two_points(x1, y1, x2, y2)
second_line = calculate_line_length_between_two_points(a1, b1, a2, b2)

if first_line >= second_line:
    closest_point(x1, y1, x2, y2)
else:
    closest_point(a1, b1, a2, b2)