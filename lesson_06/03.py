def summa(x, y=9, *args):
    print('x:', x)
    print('y:', y)
    # print('z:', z)
    print('args:', args)

    result = x + y
    for item in args:
        result += item

    print('result:', result)


print(summa(10, 20, 44))

print(summa(1, 2))

print(summa(11))

# summa()
