# Використовуючи input() ввести речення, що складається з двох слів.
# Створити 2 змінні та в кожну записати по 1 введеному слову, використовуючи
# методи строк. Створити нову змінну трьома різними способами форматування
# (фактично 3 змінні), які складаються з введених слів у зворотному порядку,
# перше слово має складатися лише з великих літер, а друге з першої великої
# літери та інших дрібних. На початку речення повинен бути знак оклику, а в
# кінці запитальний.
# Використовуючи лише атрибути функції print(), вивести початковий рядок і
# отримані різними способами форматування через роздільник "<<<>>>".
#
# *Додаткове не обов'язкове завдання: вивід зробити у файл.
#
# Приклад виконання програми:
# введене речення: "кішка охайна"
# значення першої змінної: "кішка"
# значення другої змінної: "охайна"
# нова змінна: "!ОХАЙНА Кішка?"
# Цю змінну треба створити 3-ма різними способами форматування строк
# (%-форматування, метод .format та f-string). Буде 3 нові змінні з
# однаковими значеннями.
# Вивод функції print() повинен бути наступним:
# кішка охайна<<<>>>!ОХАЙНА Кішка?<<<>>>!ОХАЙНА Кішка?<<<>>>!ОХАЙНА Кішка?


text = input("Введіть речення із двох слів: ")
splitted_text = text.split()
first_word = splitted_text[0].title()
second_word = splitted_text[1].upper()
reverse_text_1 = f"!{second_word} {first_word}?"
reverse_text_2 = "!%s %s?" % (second_word, first_word)
reverse_text_3 = "!{1} {0}?".format(first_word, second_word)
new_file = open("splitted_file.txt", "w")
print(text, reverse_text_1, reverse_text_2, reverse_text_3, sep="<<<>>>", file=new_file)
new_file.close()
