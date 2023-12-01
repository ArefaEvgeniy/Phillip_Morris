def summa(x, y, z=11, **kwargs):
    result = False
    print('x:', x)
    print('y:', y)
    print('z:', z)
    print('kwargs:', kwargs)

    return result


print(summa(y=44, x=5, t=77, c=0))
