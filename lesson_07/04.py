# Написати програму для пошуку у списку певного слова
# При цьому список може складатися з різних типів даних
# і мати не обмежену кількість вкладених один в одного списків або кортежів
# пошук зробити по всіх списках і кортежах, у тому числі і вкладених

INPUT_LIST = [
    1,
    '2',
    'cat',
    99,
    'dog',
    (4, 44, ['red', 'green', ('mother', 'father',)]),
    ['one', 'two', '55', {1, 4, 'big', True}, ['milk', 0, 'bred']],
    'End'
]


def find_word(word, input_list):
    res = False

    for item in input_list:
        if isinstance(item, (int, float, str)) and str(item) == str(word):
            res = True
            break

        elif isinstance(item, (list, tuple, set)):
            res = find_word(word, item)
            if res:
                break

    return res


def main():
    target = 100

    if find_word(target, INPUT_LIST):
        print(f'{target} found')
    else:
        print(f'{target} did not find')


main()
