import sqlite3


class Vypis:

    def vypis(self):
        connection = sqlite3.connect("pojistovna.db")
        cursor = connection.cursor()
        for row in cursor.execute("select * from pojistenci"):
            print(f"Jmeno: {row[1]}    Prijmeni: {row[2]}    Telefon: {row[3]}    Vek: {row[4]}")
        connection.close()
        return input("\nPokracujte libovolnou klavesou...")