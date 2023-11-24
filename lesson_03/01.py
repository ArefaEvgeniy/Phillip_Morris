spam = 'Spam'
spam_2, year = 'SFDSGF', 12
a = (1, 2, 3)
a_1, a_2, a_3 = a
print('a_1:', a_1)
print('a_2:', a_2)
print('a_3:', a_3)

a_1, a_2, a_3, a_4 = spam
print('a_1:', a_1)
print('a_2:', a_2)
print('a_3:', a_3)
print('a_4:', a_4)

print('-' * 50)

b_1, b_2, b_3, b_4, *b_5 = spam
print('b_1:', b_1)
print('b_2:', b_2)
print('b_3:', b_3)
print('b_4:', b_4)
print('b_5:', b_5)

q = w = 45

q += 1
w /= 9

print('q:', q)
print('w:', w)

q, w = w, q

print('q:', q)
print('w:', w)
