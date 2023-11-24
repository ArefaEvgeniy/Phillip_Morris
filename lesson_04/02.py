tempate = "Мене звати {}. мені {} років. {} класне ім'я"
tempate_2 = "Мене звати {0}. мені {1} років. {0} класне ім'я"
tempate_3 = "Мене звати {name}. мені {age} років. {name} класне ім'я"

name = input('Enter you name: ')
age = input('Enter you age: ')

print(tempate.format(name, age, name, 'TTT'))
new_string = "Мене звати {}. мені {} років. {} класне ім'я".format(name, age, name)
print(new_string)
print(tempate_2.format(name, age))
print(tempate_3.format(age=age, name=name))

print('Answer: {:.2%}'.format(34/56))

coord = (3, 5)

print('X: {0[0]}; Y: {0[1]}'.format(coord))

print('text {:<30} trtt dg fg'.format('anything'))
print('text {:>30} trtt dg fg'.format('anything'))
print('text {:^30} trtt dg fg'.format('anything'))
print('text {:-^30} trtt dg fg'.format('anything'))
