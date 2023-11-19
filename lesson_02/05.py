a = {1, 5, 0, 'a', 4, 'wer', 6, 'z', 'wer'}
a_2 = set((1, 5, 0, 'a', 4, 'wer', 6, 'z', 'wer'))
x = [1, 2, 'eer', 1, True, 'eer', None, 1, 'eer', 44, 67, 44, 0, True]

print(a)

z = 'wer'

print('wer' in a)

print(list(set(x)))

print(a_2)

a.add((999, 888))
print(a)
