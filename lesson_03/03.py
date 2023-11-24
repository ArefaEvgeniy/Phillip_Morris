a = 'AAA'
b = 'AAA'
c = True
d = True

print('a:', a)
print('id(a):', id(a))
print('b:', b)
print('id(b):', id(b))

print(a == b)
print(a is b)

print('c:', c)
print('id(c):', id(c))
print('d:', d)
print('id(d):', id(d))

f_1 = (1, 2, 3)
f_2 = (1, 2, 3)

print('f_1:', f_1)
print('id(f_1):', id(f_1))
print('f_2:', f_2)
print('id(f_2):', id(f_2))

e_1 = [1, 2, 3]
e_2 = [1, 2, 3]
print('e_1:', e_1)
print('id(e_1):', id(e_1))
print('e_2:', e_2)
print('id(e_2):', id(e_2))

print(e_1 == e_2)
print(e_1 is e_2)

e_1.pop()
print('e_1:', e_1)
print('id(e_1):', id(e_1))

print(tuple(e_1))
r = str(e_1)
print(r)
print(type(r))
print(r[:4])

g = ', '.join(['1', '2', 'tr', 'fff'])
print(g)
