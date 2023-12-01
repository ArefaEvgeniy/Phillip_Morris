name = 'Tom'


def say():
    def say_bye():
        print('Bye', name)

    name = 'Bob'
    print('Hello', name)
    say_bye()
    return name


def say_hi():
    print('Hi', name)


name = say()
say_hi()
