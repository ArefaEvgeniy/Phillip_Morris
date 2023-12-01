def summa(x, y):
    result = None
    print('x:', x)
    print('y:', y)
    if isinstance(x, (int, float)) and isinstance(y, (int, float)):
        result = x + y
    elif isinstance(x, str) or isinstance(y, str):
        result = str(x) + str(y)

    return result


print('START')
a = 10
b = 20

print(summa(b, a))

print(summa('red', 45))
