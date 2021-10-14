from math import floor


def find_point_closest_to_center(a, b, c, d):
    first_point = abs(a) + abs(b)
    second_point = abs(c) + abs(d)

    result = ()

    if first_point <= second_point:
        result = floor(a), floor(b)
    elif first_point > second_point:
        result = floor(c), floor(d)

    return result


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

closest_to_zero_coordinates = find_point_closest_to_center(x1, y1, x2, y2)
print(closest_to_zero_coordinates)