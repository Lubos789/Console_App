import sqlite3



class NovyPojisteny:

    def __init__(self):
        self.jmeno = None
        self.prijmeni = None
        self.telefon = None
        self.vek = None

    def zadej(self):
        self.jmeno = input("Zadejte jmeno pojistenoho:\n")
        self.prijmeni = input("Zadejte prijmeni:\n")
        self.telefon = input("Zadejte telefoni cislo:\n")
        self.vek = input("Zadejte vek:\n")
        connection = sqlite3.connect("pojistovna.db")
        cursor = connection.cursor()
        # cursor.execute("insert into pojistenci values (?,?,?,?)", (self.jmeno, self.prijmeni, self.telefon, self.vek))
        cursor.execute(f"INSERT INTO pojistenci (jmeno, prijmeni, telefon ,vek) "
                       f"VALUES ('{self.jmeno}', '{self.prijmeni}', '{self.telefon}', '{self.vek}')")
        connection.commit()
        connection.close()
        return input("Data byla ulozena. Pokracujte libovolnou klavesou...")
