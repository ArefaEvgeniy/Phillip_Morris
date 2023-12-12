def func():
    print('Так!')


new_func = func
func = 3
del func

new_func()
