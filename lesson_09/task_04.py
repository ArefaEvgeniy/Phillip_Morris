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
