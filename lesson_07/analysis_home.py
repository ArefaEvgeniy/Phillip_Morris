while True:
    n = input('insert  value')
    if not n.isdigit() or n == 0:
        print('try one more time')
    else:
        n = int(n)

    i = 1
    ksum = 0
    result = 0
    while i <= n:
        if i % 3 == 0:
            continue
        else:
            result = i ** 3
            ksum = result + ksum
            i += 1
    print(ksum)

    m = 1
    ksum = 0
    result = 0
    exception1 = 0
    for n in range(m, n):
        exception1 = n % 3
        if exception1 == 0:
            continue
        result = n ** 3
        ksum = result + ksum
    print(ksum)

    print('Желаете выйти? (Д/Y): ')
    print('Желаете продолжить нажмите Enter: ')
    a = input()
    if a == 'Y':
        break
    elif a == 'Д':
        break
    else:
        continue


while True:
    n = input('insert  value')
    if not n.isdigit() or n == 0:
        print('try one more time')
        continue
    else:
        n = int(n)

    i = 1
    ksum = 0
    while i <= n:
        if i % 3 != 0:
            ksum += i ** 3
        i += 1
    print(ksum)

    ksum = 0
    for item in range(1, n+1):
        if item % 3 != 0:
            ksum = item ** 3 + ksum
    print(ksum)

    a = input('Желаете выйти? (Д/Y): \nЖелаете продолжить нажмите Enter: ')
    if a.upper() in ('Y', 'Д'):
        break
