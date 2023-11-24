a = 'EEE'
source_file = open('test.txt', 'w')
print(1, 'rr', a, sep='---', file=source_file)
source_file.close()
print('OOO', 'ppp')
print(1234, sep='!!!')



