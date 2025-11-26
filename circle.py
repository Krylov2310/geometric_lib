import math


def area(r):
    return math.pi * r * r


def perimeter(r):
    return 2 * math.pi * r


r = 5
print(f'Area: {r} = {round(area(r), 2)}')
print(f'Perimeter: {r} = {round(perimeter(r), 2)}')
