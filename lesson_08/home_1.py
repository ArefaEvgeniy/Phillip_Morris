# Даний список, що складається з даних різного типу.
# Повернути новий список, де за допомогою функції map() кожен елемент типу
# int початкового списку приведений до типу str, елементи решти всіх типів
# передаються в новий список без зміни їх типу.
# У якості вхідної функції в map використовувати lambda-функцію.
# values = [1, 2, '3', 'forth', 'end', 99, True, None]


values = [1, 2, '3', 'forth', 'end', 99, True, None]
new_value = list(map(lambda x: str(x) if isinstance(x, int) and not isinstance(x, bool) else x, values))
print(new_value)
