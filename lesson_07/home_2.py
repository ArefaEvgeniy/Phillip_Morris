# Написати лямбда-функцію визначальну парне/непарне.
# Функція приймає параметр (число) і якщо парне, видає слово “парне”,
# якщо ні - то “не парне”.
#
# *Додаткове не обов'язкове завдання:
# лямбда-функція вміє визначати як парне чи парне, а й число нуль.


number = int(input('введите число: '))
func = lambda x: 'парне' if x % 2 == 0 else 'непарне'
print(func(number))

print((lambda x: 'парне' if x % 2 == 0 and x != 0 else 'непарне' if x != 0 else 'нуль')(number))
