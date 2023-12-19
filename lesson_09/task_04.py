# Витягти інформацію з html-файлу
# Допустимо, потрібно витягти інформацію з html-файлу, укладену між td> і td, крім першого стовпця.
# Приклад вмісту html-файлу:

import re


html = """
<p>Table of people</p>
<table>
     <tr>
         <td>1SurnameName</td><td>1SurnameName2LiamOlivia3MasonSophia4JacobIsabella5WilliamAva6EthanMia7MichaelEmily</td>
         <td>1SurnameName2FosterLeon3StaffordGerald4RichKaren5KnightLinda6FletcherScarlett7PattersonWalter8UnderwoodBrian9GordonHilary10CarterWilliam11GarrettDylan12HutchinsonKerry13RileyJus</td>
         <td>-</td>
     </tr>
</table>
"""

result = re.findall(r'<td>(.*?)</td>', html)
print(result)

result_2 = []
for item in result:
    res = re.findall(r'([2-9]|\d\d)([A-Z][A-Za-z]+)([A-Z][A-Za-z]+)', item)
    print(res)
    result_2.extend(list(map(lambda x: f"{x[1]} {x[2]}", res))) if res else ...

print(result_2)
