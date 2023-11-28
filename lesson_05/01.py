c = int(input())

q = 0
result = 1
while c > q:
    q += 1
    print('q:', q)
    result *= q
else:
    print('ELSE')

print('result:', result)
