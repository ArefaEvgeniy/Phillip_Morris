a = {1: 's', 2: 'rr', 4: 55, "Арефа Євген": [111, 444, 333]}

print(len(a))

print(a[2])
print(a.get(44, 'No key'))

a.update({44: 'RRR'})
print(a.get(44, 'No key'))

print(a.keys())
print(a.values())
print(a.items())

print(a.get("Арефа Євген"))
a.update({"Арефа Євген": 'YYYYY'})
print(a)

d = a.pop("Арефа Євген")
print(a)
print(d)

a.update({0: {'r': {77: 99}}})
print(a)
print(a.get(0).get('r')[77])
