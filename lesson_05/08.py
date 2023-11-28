for item in [1, '0', 100, 2, 'RR', 3, 4, 'RT4565', 5]:
    print(item, end=' ')

print()
for item in (1, '0', 100, 2, 'RR', 3, 4, 'RT4565', 5):
    print(item, end=' ')

print()
for item in {1, '0', 100, 2, 'RR', 3, 4, 'RT4565', 5}:
    print(item, end=' ')

print()
for item in {1: '0', 100: 3, 'RR': 3, 4: 'RT4565', 5: 'END'}:
    print(item, end=' ')

print()
for item in {1: '0', 100: 3, 'RR': 3, 4: 'RT4565', 5: 'END'}.values():
    print(item, end=' ')

print()
for item in {1: '0', 100: 3, 'RR': 3, 4: 'RT4565', 5: 'END'}.keys():
    print(item, end=' ')

print()
for item in {1: '0', 100: 3, 'RR': 3, 4: 'RT4565', 5: 'END'}.items():
    print(item, end=' ')
