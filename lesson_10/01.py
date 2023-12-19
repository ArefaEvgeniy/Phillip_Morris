japan_str = 'ぁぃえおき げず㍿ボ゛'
japan_char = '㍿'

color = 'red'
name = 'Tom'
surname = 'Арефа'
surname_2 = 'Apeфa'

print(name.encode())
print(type(name.encode()))
print(len(name.encode()))

print(surname.encode())
print(type(surname.encode()))
print(len(surname.encode()))

print(surname_2.encode())
print(type(surname_2.encode()))
print(len(surname_2.encode()))

print(japan_char.encode())
print(type(japan_char.encode()))
print(len(japan_char.encode()))

print(japan_char.encode('utf-16'))
print(type(japan_char.encode('utf-16')))
print(len(japan_char.encode('utf-16')))

new_value = japan_char.encode()
print(new_value.decode('latin-1'))
