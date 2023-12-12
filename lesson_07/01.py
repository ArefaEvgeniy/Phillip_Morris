def area(b, h):
    return 0.5 * b * h


print(area(3, 2))
print(area(5, 3))

area_2 = lambda b, h: 0.5 * b * h
print(area_2(3, 2))
print(area_2(5, 3))
