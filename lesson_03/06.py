a = 1
b = 2.5
c = '2'
a_1 = str(a)
c_1 = int(c)

print(a + b)
print(type(a + b))

print(a + c_1)
print(type(a + c_1))

print(a_1 + c)
print(type(a_1 + c))

q = int(a_1 + c) + a
print(q)
print(type(q))

print(list('Black Jack'))

print(bool(-1000))
print(bool(0.000001))
print(bool(0))

print(bool('ertff'))
print(bool(''))

print(bool([1, 2, 3]))
print(bool([]))

print(bool({1: 2}))

a = []

if a:
    print('FULL')
else:
    print('EMPTY')
