a = [1, 2, 'eer', True, 'eer', None, [5, 66, 777, 0], 'eer']

print(type(a))
print(a)
print(len(a))
print('eer' in a)
print(2 in a and 'eer' in a)

z = a.append(888)
print(a)
print(z)

a.insert(2, 'Black')
print(a)

a[2] = 'New'
print(a)

print(a[7])
print(a[7][2])

print('-' * 50)
a.remove('eer')
print(a)

x = a.pop()
print(a)
print(x)

x = a.pop(1)
print(a)
print(x)

del a[1]
print(a)

b = ['a', 'd0', 'rrr']

a.extend(b)
print(a)
