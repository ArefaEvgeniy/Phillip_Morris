def func(a: str, b: int = 77) -> bool:
    """
    This my function
    This is a simple object
    """
    z = a + '!!!'
    if len(z) > 4:
        res = False
    else:
        res = True
    print('a')
    print(b + 10)
    return res


print(func('r', 22))
print(func.__annotations__)
print(func.__doc__)
