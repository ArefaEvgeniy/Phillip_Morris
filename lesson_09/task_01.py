# Повернути домени зі списку email-адрес
input_str = 'abc.test@gmail.com, xyz@test.in.ua, test.first@analyticsvidhya.com, first.test@rest.biz'


import re

result = re.findall(r'@(\w+.\w+.?\w+)', input_str)
print(result)
