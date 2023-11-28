# Ввести число, перевірити, що було введено саме число.
# Звести його в куб.
# Реалізацію обернути у вічний цикл із можливістю вийти з нього на запит.

while True:
    input_value = input('Enter your number: ')

    if not input_value.isdigit():
        continue

    print(f'Куб введего числа = {int(input_value) ** 3}')

    answer = input("Do you wont exit? (Y/Т): ").upper()
    if answer in ('Y', 'Т'):
        break
