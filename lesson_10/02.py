# Дана змінна artist_bytes у байтовому вигляді.
# Декодувати її в юнікод і вивести на екран.
# Декодування значення закодувати в кодуванні 'Latin1'


artist_bytes = b'Tage \xc3\x85s\xc3\xa9n'
print(artist_bytes)
print(len(artist_bytes))

artist_str = artist_bytes.decode('utf-8')
print(artist_str)

artist_bytes_latin_1 = artist_str.encode('Latin-1')
print(artist_bytes_latin_1)
print(len(artist_bytes_latin_1))

artist_str_new = artist_bytes_latin_1.decode('Latin-1')
print(artist_str_new)
