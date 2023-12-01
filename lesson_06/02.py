def summa(x, y=33, z=None):
    result = None
    print('x:', x)
    print('y:', y)
    print('z:', z)
    if isinstance(x, (int, float)) and isinstance(y, (int, float)):
        result = x + y
    elif isinstance(x, str) or isinstance(y, str):
        result = str(x) + str(y)

    return result


print(summa(10, 20, 44))

print(summa(1, 2))

print(summa(11))
