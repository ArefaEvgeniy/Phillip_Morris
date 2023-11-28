x = 20

a = []
for item in range(x + 1):
    a.append(item)

print(a)

a_1 = [i ** 2 for i in range(x + 1)]
print(a_1)

a_2 = [i ** 2 for i in range(x + 1) if i % 3 == 0]
print(a_2)

b = 'weZЮr454gЩfkjTIEp3rt6УУУYККК8ujjh00РРР9TfААg4'
b_new = [int(i) for i in b if i.isdigit()]
b_1 = [int(i) for i in b if '0' <= i <= '9']
b_2 = [i for i in b if 'A' <= i <= 'Z']
b_3 = [i for i in b if 'А' <= i <= 'Ю' or 'A' <= i <= 'Z']
print(b_new)
print(b_1)
print(b_2)
print(b_3)
