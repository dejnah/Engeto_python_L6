#ZKONTROLUJ ZIP A  ZKUS SI TU LOGIKU VYMYSLET

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
#8. Úvodní rozhodovací podmínky máš napsané. Teď pojď doplnit zbytek a samozřejmě výstup.
#9. dopiš logiku ve smyslu hry (např. hráč má "kamen", počítač "nuzky", tedy vyhrává hráč), kdy do proměnné vysledek = "Vyhrává hráč!",
#10. zbytek podmínek máš zapsaných z předchozího kroku a proces je kompletní,
#11. pro každý krok smyčky for ještě doplň výstup jako: "Výsledek: <VYSLEDEK>",
#12. ukázkový výstup potom může vypadat následovně:

import random

moznosti = ['kamen', 'nuzky', 'papir']
hrac_volby = list()
pocitac_volby = list()

while len(hrac_volby) < 3 and len(pocitac_volby) < 3:
    hrac_volby.append(random.choice(moznosti))
    pocitac_volby.append(random.choice(moznosti))

print(hrac_volby)
print(pocitac_volby)

for volba_hrac, volba_pocitac in zip(hrac_volby, pocitac_volby):
    if volba_hrac == volba_pocitac:
        vysledek = "Remíza!"
    elif volba_hrac == "nuzky" and volba_pocitac == "kamen":
        vysledek = "Vyhrává počítač!"
    elif volba_hrac == "kamen" and volba_pocitac == "papir":
        vysledek = "Vyhrává počítač!"
    elif volba_hrac == "papir" and volba_pocitac == "nuzky":
        vysledek = "Vyhrává počítač!"
    else:
        vysledek = "Vyhrává hráč!"
    print(f"Výsledek: {vysledek}")
