# -> generate random number
# -> input and validate number
# -> check numbers


def generate_random_number(min_number, max_number):
    res = None
    ...
    return res


def input_number():
    while True:
        number = input('Input your number: ')
        if number and number.isdigit():
            break
        print('Something is wrong!')
    return number


def check_numbers(secret_number, user_number, attempt):
    res = None
    ...
    return res


def main():
    max_attempt = 3
    min_number = 1
    max_number = 10

    while True:
        secret_number = generate_random_number(min_number, max_number)
        for attempt in range(1, max_attempt + 1):
            user_number = input_number()
            if check_numbers(secret_number, user_number, attempt) is True:
                break

        answer = input('Do yoo want exit(Y/N)').upper()
        if answer == 'Y':
            print('Bye')
            break


main()
