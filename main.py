from novy_pojisteny import NovyPojisteny
from vypis import Vypis
from vyhledej2 import Vyhledej2
from delete import Delete
from logo import logo
import os
import sqlite3

# connection = sqlite3.connect("pojistovna.db")
# cursor = connection.cursor()
#cursor.execute("create table new_pojisteni(id integer primary key, jmeno text, prijmeni text, telefon text, vek text)")

clear = lambda: os.system('cls')
cls = lambda: print('\n'*100)
akce = 0

while akce != 5:
    clear()
    cls()
    print(logo)
    print("---------------------------------\nEvidence pojistenych\n---------------------------------")
    akce = int(input("Vyberte si akci:\n1 - Pridat noveho pojisteneho\n2 - Vypsat vsechny pojistene\n"
                     "3 - Vyhledat pojisteneho\n4 - Vymazat pojisteneho\n5 - Konec\n"))

    if akce == 1:
        novy_pojisteny = NovyPojisteny()
        novy_pojisteny.zadej()

    elif akce == 2:
        vypis = Vypis()
        vypis.vypis()

    elif akce == 3:
        vyhledej = Vyhledej2()
        result = vyhledej.hledej2()
        if not result == True:
            input("Hledany pojistenec nenalezen!!!\n\nPokracujte libovolnou klavesou...")
        else:
            input("\n\nPokracujte libovolnou klavesou...")

    elif akce == 4:
        delete = Delete()
        result = delete.delete()
        if not result == True:
            input("Nelze odstranit, zaznam nenalezen!!!\n\nPokracujte libovolnou klavesou...")

    else:
        if akce == 5:
            pass
        else:
            print("Zadali jste chybnou volbu")
            input("Pokracujte libovolnou klavesou...")

