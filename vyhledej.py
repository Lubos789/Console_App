import sqlite3


class Vyhledej:

    def __init__(self):
        self.jmeno = input("Zadejte jmeno pojisteneho:\n")
        self.prijmeni = input("Zadejte prijmeni pojisteneho:\n")

    def hledej(self):
        connection = sqlite3.connect("pojistovna.db")
        cursor = connection.cursor()
        for row in cursor.execute("select * from pojistenci"):
            if row[1] == self.jmeno and row[2] == self.prijmeni:
                print(f"\n{row[1]}    {row[2]}    {row[3]}    {row[4]}")
                input("\nPokracujte libovolnou klavesou...")
                connection.close()
                return True

# vyresti dva s stejnym jmenem