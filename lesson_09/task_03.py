# Витягти слова, що починаються на голосну
# 'AV is largest Analytics community of India'

import re

data = 'AV is largest Analytics 55 community of India 88745'
result = re.findall(r'\b[aeiouAEIOU]\w+', data)
print(result)
