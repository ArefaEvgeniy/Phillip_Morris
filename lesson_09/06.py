import re

str = "AV Analytics AV"

result = re.match('AV Analytics', str)
if result:
    print(result.group(0))
    print(result.start())
    print(result.end())
else:
    print('Not found')

print('-' * 50)

result = re.search('AV', str)
if result:
    print(result.group(0))
    print(result.start())
    print(result.end())
else:
    print('Not found')

print('-' * 50)

result = re.findall('AV', str)
print(result)

print('-' * 50)

result = re.split('AV', str)
print(result)

print('-' * 50)

result = re.sub('A', 'SSS', str)
print(result)

print('-' * 50)

result = re.sub('\s+', ' ', 'jhgu     kjhfw dghjgd   uytew       wdjfg js     eutyg                   errege')
print(result)

print('-' * 50)

pattern = re.compile('AV')
result = pattern.findall(str)
print(result)

result = pattern.sub('TTT', str)
print(result)
