import sqlite3


class Vyhledej2:

    def __init__(self):
        self.jmeno = input("Zadejte jmeno pojisteneho:\n")
        self.prijmeni = input("Zadejte prijmeni pojisteneho:\n")
        print()

    def hledej2(self):
        check = False
        connection = sqlite3.connect("pojistovna.db")
        cursor = connection.cursor()
        for row in cursor.execute(f"select * from pojistenci where jmeno = '{self.jmeno}' and prijmeni = '{self.prijmeni}'"):
            print(f"{row[1]}    {row[2]}    {row[3]}    {row[4]}")
            if row[1] != None:
                check = True
        connection.close()
        return check
