a = 50
res = 11

if a > 100:
    res = True
elif a > 10:
    res = None
else:
    res = False

print('res:', res)

res = True if a > 100 else (None if a > 10 else False)
print('res:', res)
