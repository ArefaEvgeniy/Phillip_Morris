a = [1, 5, 8, 33, 0]


def func(x):
    print('start x:', x)
    x.append(100)
    print('end x:', x)


print('before a:', a)
func(a[:])
print('after a:', a)
