a = [88, 0, 'ee', 99]    # a = 3437a773fc24   878767400044


def func(x):             # x = 878767400044
    print('x:', x)
    x.append(True)
    print('x:', x)


print('a before:', a)
func(a[:])
print('a after:', a)
