from sa import *

db1 = SqlAlchemyCreate('sqlite:///Lista Prezentów.db', "Prezenty_2020")
db1.sql_create_5col_cstr("id", Integer, "Imię_Obdarowanego",
String, "Pomysł_na_prezent", String, "Cena", Integer, "Miejsce_zakupu", String,
)

db2 = SqlAlchemyWrite('sqlite:///Lista Prezentów.db', """INSERT INTO
Prezenty_2020(id, Imię_Obdarowanego, Pomysł_na_prezent, Cena, Miejsce_zakupu)
VALUES(:id, :Imię_Obdarowanego, :Pomysł_na_prezent, :Cena, :Miejsce_zakupu)""")
data = ({ "id": 1, "Imię_Obdarowanego": "Maciej", "Pomysł_na_prezent": "Trackpad",
"Cena": "700", "Miejsce_zakupu": "Katowice" },
{ "id": 2, "Imię_Obdarowanego": "Nina", "Pomysł_na_prezent": "Brak",
"Cena": None, "Miejsce_zakupu": "Brak" },
{ "id": 3, "Imię_Obdarowanego": "Ola", "Pomysł_na_prezent": "Wycieczka",
"Cena": "700", "Miejsce_zakupu": "Kraków" },
{ "id": 4, "Imię_Obdarowanego": "Stanisław", "Pomysł_na_prezent": "Wódka",
"Cena": "40", "Miejsce_zakupu": "Chorzów" },
{ "id": 5, "Imię_Obdarowanego": "Łukasz", "Pomysł_na_prezent": "Słuchawki",
"Cena": "90", "Miejsce_zakupu": "Poznań" })
db2.sql_write(data)

db3 = SqlAlchemyWrite('sqlite:///Lista Prezentów.db', """SELECT * FROM
Prezenty_2020""")
db3.sql_any_print()

db4 = SqlAlchemyWrite('sqlite:///Lista Prezentów.db', """UPDATE Prezenty_2020
SET Pomysł_na_prezent = "Rower" WHERE id = 3 """)
db4.sql_any()

db5 = SqlAlchemyWrite('sqlite:///Lista Prezentów.db', """SELECT * FROM
Prezenty_2020 WHERE id = 3 """)
db5.sql_any_print()

'''Wykonałbym to poprzez:
db6 = SqlAlchemyWrite('sqlite:///Lista Prezentów.db', """ALTER TABLE
Prezenty_2020 DROP Miejsce_zakupu""")
db6.sql_any()
ale SQLite nie pozwala na usunięcie kolumny poprzez komendę, zrobiłem to w
aplikacji standalone. Wykonałem zgodnie z
stackoverflow.com/questions/5938048/delete-column-from-sqlite-table/5987838'''

db6 = SqlAlchemyWrite('sqlite:///Lista Prezentów.db', """SELECT Imię_Obdarowanego
 FROM Prezenty_2020 WHERE id = 3""")
db6.sql_any_print()
db6 = SqlAlchemyWrite('sqlite:///Lista Prezentów.db', """SELECT Imię_Obdarowanego
 FROM Prezenty_2020 WHERE id = 4""")
db6.sql_any_print()
db6 = SqlAlchemyWrite('sqlite:///Lista Prezentów.db', """SELECT Imię_Obdarowanego
 FROM Prezenty_2020 WHERE id = 5""")
db6.sql_any_print()
