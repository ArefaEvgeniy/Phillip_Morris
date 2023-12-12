from datetime import datetime


def factorial_1(n):
    q = 0
    result = 1
    while n > q:
        q += 1
        result *= q
    return result


def factorial_2(n):                     # 5     4       3       2       1
    if n <= 1:
        return 1
    else:
        return n * factorial_2(n - 1)   # 5 * 24 = 120
                                        # 4 * 6 = 24
                                        # 3 * 2 = 6
                                        # 2 * 1 = 2
                                        # 1
now = datetime.now()
print(factorial_1(900))
print('Time spend of factorial_1:', datetime.now() - now)
now = datetime.now()
print(factorial_2(900))
print('Time spend of factorial_2:', datetime.now() - now)
