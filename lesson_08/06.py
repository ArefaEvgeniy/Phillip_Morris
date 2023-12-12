def talk(type='shout'):
    def whisper(a='yes'):
        return f'{a.lower()}...'

    def shout(a='yes'):
        return f'{a.title()}!'

    if type == 'shout':
        res = shout
    else:
        res = whisper

    return res


print(talk()('alex'))
