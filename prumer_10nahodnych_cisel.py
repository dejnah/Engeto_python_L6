#1. Nahraj z knihovny `random` objekt pro výběr 10 náhodných čísel z intervalu **0-1000**,
#2. nahraj z knihovny `statistics` objekt pro výpočet průměrné hodnoty z *iterovalného* objektu pod alias `mean`,
#3. do proměnné `nahodna_cisla` ulož **10 náhodných celých čísel**,
#4. do proměnné `prumer` ulož průměrnou hodnotu,
#5. výsledek na závěr vypiš ve formátu:`Průměr náhodných čísel je:  <prumer>`.

from random import choices   #nahodne vybere zadany pocet (k) cisel v rozsahu
from statistics import mean  #udela prumer (ze zadane promenne)

nahodna_cisla = choices(range(1001), k=10)
prumer = mean(nahodna_cisla)
print(f"Průměr náhodných čísel je: {prumer}")
