a = [1, 5, 8, 33, 0]


def func(x=None):
    if x is None:
        x = [1, 2]
    x.append(len(x))
    return x


b = func()
print(b)
a = func(a)
print(a)
a = func(a)
print(a)
c = func()
print(c)
d = func()
print(d)
