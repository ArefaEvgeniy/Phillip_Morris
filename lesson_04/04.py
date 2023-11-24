# Запросити у користувача два цілих числа.
# Вивести строку виду "2 плюс 3 дорівнює 5"

import datetime


num_1 = int(input('Enter first number: '))
num_2 = int(input('Enter second number: '))

now = datetime.datetime.now()
print('%s плюс %s дорівнює %s' % (num_1, num_2, num_1 + num_2))
print('Spend time:', datetime.datetime.now() - now)

now = datetime.datetime.now()
print('{0} плюс {1} дорівнює {2}'.format(num_1, num_2, num_1 + num_2))
print('Spend time:', datetime.datetime.now() - now)

now = datetime.datetime.now()
print(f'{num_1} плюс {num_2} дорівнює {num_1 + num_2}')
print('Spend time:', datetime.datetime.now() - now)
