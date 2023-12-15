from langdetect import detect, detect_langs


str_1 = 'ぁぃえおき げず㍿ボ'
str_2 = 'Rodzice mają prawo pierwszeństwa w wvborze nauczania, które ma być dane ich dzieciom.'
str_3 = 'шла Саша по шоссе'

print(detect(str_1))
print(detect(str_2))
print(detect(str_3))

print(detect_langs(str_1))
print(detect_langs(str_2))
print(detect_langs(str_3))
