# Написать декоратор, который выдаст:
# </----------\>
# помидоры
# --ветчина--
# ~салат~
# <\______/>


def decorator_1(func):
    def wrapper(*args, **kwargs):
        print('помидоры')
        result = func(*args, **kwargs)
        print('~салат~')
        return result

    return wrapper


def decorator_2(func):
    def wrapper(*args, **kwargs):
        print('</----------\>')
        result = func(*args, **kwargs)
        print('<\______/>')
        return result

    return wrapper


@decorator_2
@decorator_1
def sandwich(food="--ветчина--"):
    print(food)


@decorator_1
def banana(food="--банан--"):
    print(food)


# sandwich = decorator_1(sandwich)

sandwich('ковбаса')

print('-' * 50)

banana()
