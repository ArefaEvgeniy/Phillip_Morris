# Витягти усі дати з рядка
# 'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67 -8945 12-01-2009 incorrect data 23-06-1657 New 15-09-2001'

import re

data = 'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67 -8945 12-01-2009 incorrect data 23-06-1657 New 15-29-2001'

result = re.findall(r'(\d{2})-0?1?\d-(20\d{2})', data)
print(result)

for item in result:
    print(f'{item[0]}-{item[1]}')
