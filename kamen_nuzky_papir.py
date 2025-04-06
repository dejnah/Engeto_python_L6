#naimportuj knihovnu random
#zapiš si tyto proměnné
#Nachystej smyčku while, která bude probíhat tak dlouho, dokud
#1. hrac_volby bude obsahovat přesně 3 náhodně vybrané hodnoty z moznosti
#2. pocitac_volby bude obsahovat  přesně 3 náhodně vybrané hodnoty z moznosti
#3. jakmile budou hrac_volby a pocitac_volby obě obsahovat 3 různé hodnoty z proměnné moznosti, smyčka while skončí.
#4. Postupně projdi a porovnej volby hráče, počítače a rozhodni o tom, kdo vyhrál které kolo.
#5. Projdi současně jednotlivé volby jak v hrac_volby, tak pocitac_volby
#6. pokud mají hrac i pocitac stejnou volbu (např. "kamen" a "kamen"), ulož do proměnné vysledek = "Remíza!"
#7. pro všechny ostatní případy zapiš vysledek = "Vyhrává počítač!",

import random

moznosti = ['kamen', 'nuzky', 'papir']
hrac_volby = list()
pocitac_volby = list()

while len(hrac_volby) < 3:
    hrac_volby.append(random.choice(moznosti))
    while len(pocitac_volby) < 3:
        pocitac_volby.append(random.choice(moznosti))
print(hrac_volby)
print(pocitac_volby)
