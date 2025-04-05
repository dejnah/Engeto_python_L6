#1. Nahraj knihovnu `math`,
#2. pro zadaný tuple `polomery`, vypočítej plochu kruhů (prozkoumej objekty v knihovně `math`, kde potřebuješ dohledat mocniny a konstantu pí),
#3. vypočítané plochy potom ukládej do proměnné `plochy`.


#moje řešení
import math

polomery = (1, 2, 3, 4, 5)
plochy = list()


for polomer in polomery:
    plocha = (math.pi * (polomer ** 2)) 
    plochy.append(plocha)
print(plochy)

#----------------------------------#
#řešení se více moduly

import math

polomery = [1, 2, 3, 4, 5]
plochy = list()

for polomer in polomery:
    plochy.append(math.pow(polomer, 2) * math.pi)
else:
    print(plochy)
