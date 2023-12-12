# Створити функцію lambda, яка приймає на вхід список імен
# та виводить їх у форматі “Hello, {name}” до іншого списку.
# Всі імена повинні бути написані малими літерами і з великою першою

list_names = ['TOM', 'Jack', 'jessy', 'LaRi']

make_list = lambda x: [f'Hello, {i.title()}' for i in x]
print(make_list(list_names))
