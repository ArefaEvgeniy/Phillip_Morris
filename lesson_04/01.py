tempate = "Мене звати %s. мені %s років. %s класне ім'я"
tempate_2 = "Мене звати %(name)s. мені %(age)s років. %(name)s класне ім'я"

name = input('Enter you name: ')
age = input('Enter you age: ')

print(tempate % (name, age, name))
print("Мене звати %s. мені %s років. %s класне ім'я" % (name, age, 'Karl'))

print(tempate_2 % {'age': age, 'name': name})
print(tempate_2 % {'age': 55, 'name': 'Rick', 'key': 'TTT'})
