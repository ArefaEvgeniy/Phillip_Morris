import copy

a = [1, 2, 3, 4]    # 1: 2234542, 2: 665fa455, 3: 5675334, 4: 11100001,     2234542, 665fa455, 5675334, 11100001
# a: 112209aa

first_copy = copy.copy(a)
second_copy = a[:]

print('a:', a)
print('id(a):', id(a))
print('first_copy:', first_copy)
print('id(first_copy):', id(first_copy))
print('second_copy:', second_copy)
print('id(second_copy):', id(second_copy))

first_copy.append('0')
second_copy.pop()
print('a:', a)
print('first_copy:', first_copy)
print('second_copy:', second_copy)
