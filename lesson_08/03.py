# Створити власну версію вбудованої функції sum(). Функція sum() повертає
# суму кубів всіх елементів об'єкта, що ітерується, переданих їй.


from functools import reduce

numbers = [3, 4, 6, 9, 34, 12]


def custom_func(a, x):
    return a + x ** 3


result_1 = reduce(custom_func, numbers, 0)
print(result_1)

result_2 = reduce(lambda a, x: a + x ** 3, numbers, 0)
print(result_2)
