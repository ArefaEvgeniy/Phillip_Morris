a = " Hello, world    "
a_2 = "Hello, world red blue green black"
b = '44'
c = 'bLuE'

print(a[0].isdigit())
print(a[0].isalpha())

print(b.isdigit())
print(b.isalpha())

print(a.lower())
print(a)
print(a.upper())

print(a.title())
print(a.capitalize())

a.find('l')
z = a.find('l')

print(a)
print(z)

print(a[z+1:].replace('l', 'z', 2))

print(a.strip())
print(a_2.split())

# print(('a' <= simbol <= 'z') or ('A' <= simbol <= 'Z'))

print('ello' in a)
