a = 1
c = 0
d = [1, 2, 3]
f = None

if f is None:
    print('F is None')
elif d:
    print('a more than 10')
elif a > 0:
    print('A is positive')
    c = 100
    if a < -5:
        print('a more than 5')
        c = 55
    c += 12
else:
    print('ELSE')

print('END')
print('c:', c)
