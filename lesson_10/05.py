# Є текстовий файл. Надрукувати:
# a) його перший рядок;
# b) його п'ятий рядок;
# c) його перші 5 рядків;
# d) весь файл.


with open('test.txt') as f:
    print(f.readline().strip())


with open('test.txt') as f:
    a = f.readlines()
for index, item in enumerate(a):
    if index == 4:
        print(item)


with open('test.txt') as f:
    a = f.readlines()
for index, item in enumerate(a):
    if index <= 4:
        print(item.strip())
