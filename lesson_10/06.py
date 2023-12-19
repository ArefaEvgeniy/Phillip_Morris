# Слово "ciào" якому в кодуванні "utf-8" відповідає b'ci\xc3\xa0o',
# записати в текстовий файл у кодуванні "Latin1".
# Потім прочитати його та вивести на екран.


data = b'ci\xc3\xa0o'

with open('06.txt', 'w', encoding='Latin_1') as f:
    f.write(data.decode())


with open('06.txt', 'r', encoding='Latin_1') as f:
    a = f.read()
print(a)

with open('06.txt', 'rb') as f:
    a_2 = f.read()
print(a_2.decode('Latin_1'))
