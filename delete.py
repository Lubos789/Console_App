import sqlite3


class Delete:

    def __init__(self):
        self.jmeno = input("Zadejte jmeno pojisteneho, ktereho chcete vymazat:\n")
        self.prijmeni = input("Zadejte prijmeni pojisteneho, ktereho chcete vymazat:\n")

    def delete(self):
        connection = sqlite3.connect("pojistovna.db")
        cursor = connection.cursor()
        for row in cursor.execute(f"select * from pojistenci where jmeno = '{self.jmeno}' and prijmeni = '{self.prijmeni}'"):
            cursor.execute(f'DELETE FROM pojistenci WHERE uzivatele_id = "{row[0]}"')
            connection.commit()
            connection.close()
            input("Zaznam byl odstranen. Pokracujte libovolnou klavesou...")
            return True




    # def delete(self):
    #     connection = sqlite3.connect("pojistovna.db")
    #     cursor = connection.cursor()
    #     for row in cursor.execute("select * from pojistenci"):
    #         if row[1] == self.jmeno and row[2] == self.prijmeni:
    #             connection.close()      #pridano
    #             connection = sqlite3.connect("pojistovna.db")
    #             cursor = connection.cursor()
    #             # cursor.execute(f'DELETE FROM pojistenci WHERE jmeno = "{self.jmeno}" AND prijmeni = "{self.prijmeni}"')
    #             # nevyresi, stejne nevim ktereho ze dvou stejnych chce uzivatel smazat, nesmaze vsechny ale jen jednoho
    #             cursor.execute(f'DELETE FROM pojistenci WHERE uzivatele_id = "{row[0]}"')
    #             connection.commit()
    #             connection.close()
    #             input("Zaznam byl odstranen. Pokracujte libovolnou klavesou...")
    #             return True