import copy

a = [1, 2, 3, 4, ['a', 'b']]    # 1: 2234542, 2: 665fa455, 3: 5675334, 4: 11100001,  3345533    2234542, 665fa455, 5675334, 11100001

                                     # a: 140079684463808    2234542, 665fa455, 5675334, 11100001, 3345533
first_copy = copy.deepcopy(a)        # first_copy: 140079684023232    2234542, 665fa455, 5675334, 11100001, 4456663
second_copy = copy.deepcopy(a)       # second_copy: 140079683986368    2234542, 665fa455, 5675334, 11100001, 89987000

print('a:', a)
print('id(a):', id(a))
print('first_copy:', first_copy)
print('id(first_copy):', id(first_copy))
print('second_copy:', second_copy)
print('id(second_copy):', id(second_copy))

first_copy[4].append('0')
second_copy.pop(0)
print('a:', a)
print('first_copy:', first_copy)
print('second_copy:', second_copy)
