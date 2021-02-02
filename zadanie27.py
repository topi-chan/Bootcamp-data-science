from sa2 import *

db1 = SqlAlchemyCreate('sqlite:///Pracownicy.db', "Pracownicy")
db1.sql_create_5col_cstr_2("id", Integer, "Imię",
String, "Nazwisko", String, "Wiek", Integer, "Kurs", String,
)
db2 = SqlAlchemyWrite('sqlite:///Pracownicy.db', """INSERT INTO
Pracownicy(id, Imię, Nazwisko, Wiek, Kurs)
VALUES(:id, :Imię, :Nazwisko, :Wiek, :Kurs)""")
data = ({ "id": 1, "Imię": "Anna", "Nazwisko": "Topolewski",
"Wiek": 32, "Kurs": "Python" },
{ "id": 2, "Imię": "Magdalena", "Nazwisko": "Moj",
"Wiek": 27, "Kurs": "Frontend" },
{ "id": 3, "Imię": "Mateusz", "Nazwisko": "Jędryka",
"Wiek": 28, "Kurs": "DS" },
{ "id": 4, "Imię": "Aneta", "Nazwisko": "Woźniak",
"Wiek": 45, "Kurs": "UX" },
{ "id": 5, "Imię": "Anna", "Nazwisko": "Chmiel",
"Wiek": 24, "Kurs": "Java" },
{ "id": 6, "Imię": "Patryk", "Nazwisko": None,
"Wiek": 28, "Kurs": "Tester" },
{ "id": 7, "Imię": "Anna", "Nazwisko": None,
"Wiek": 32, "Kurs": "Python" },
{ "id": 8, "Imię": "Magdalena", "Nazwisko": "Szymański",
"Wiek": 27, "Kurs": "Frontend" },
{ "id": 9, "Imię": "Mateusz", "Nazwisko": "Dąbrowski",
"Wiek": 28, "Kurs": "DS" },
{ "id": 10, "Imię": "Aneta", "Nazwisko": "Kozłowski",
"Wiek": 45, "Kurs": "UX" },
{ "id": 11, "Imię": "Anna", "Nazwisko": "Mazur",
"Wiek": 24, "Kurs": None },
{ "id": 12, "Imię": "Patryk", "Nazwisko": "Lewandowski",
"Wiek": 28, "Kurs": "Tester" },
{ "id": 13, "Imię": "Anna", "Nazwisko": "Nowak",
"Wiek": 32, "Kurs": "Python" },
{ "id": 14, "Imię": "Magdalena", "Nazwisko": "Kowalski",
"Wiek": 27, "Kurs": "Frontend" },
{ "id": 15, "Imię": "Mateusz", "Nazwisko": "Wiśniewski",
"Wiek": 28, "Kurs": "DS" },
{ "id": 16, "Imię": "Aneta", "Nazwisko": "Wójcik",
"Wiek": 45, "Kurs": "UX" },
{ "id": 17, "Imię": "Anna", "Nazwisko": "Jankowski",
"Wiek": 24, "Kurs": "Java" },
{ "id": 18, "Imię": "Patryk", "Nazwisko": "Kowalczyk",
"Wiek": 28, "Kurs": "Tester" },
{ "id": 19, "Imię": "Mateusz", "Nazwisko": None,
"Wiek": 28, "Kurs": "DS" },
{ "id": 20, "Imię": "Aneta", "Nazwisko": "Wojnarz",
"Wiek": 45, "Kurs": "UX" })
db2.sql_write(data)

db3 = SqlAlchemyWrite('sqlite:///Pracownicy.db', """SELECT *
 FROM Pracownicy WHERE Wiek = 30""")
db3.sql_any_print()

db4 = SqlAlchemyWrite('sqlite:///Pracownicy.db', """SELECT *
 FROM Pracownicy WHERE Wiek <= 30""")
db4.sql_any_print()

db5 = SqlAlchemyWrite('sqlite:///Pracownicy.db', """SELECT *
 FROM Pracownicy WHERE Nazwisko LIKE '%ski%'""")
db5.sql_any_print()

db6 = SqlAlchemyWrite('sqlite:///Pracownicy.db', """SELECT * FROM Pracownicy
WHERE id = 1 OR id IS 4 OR id IS 7 OR id IS 18 OR id IS 20""")
db6.sql_any_print()

db7 = SqlAlchemyWrite('sqlite:///Pracownicy.db', """SELECT * FROM Pracownicy
WHERE (id IS NOT NULL AND Imię IS NOT NULL AND Nazwisko IS NOT NULL
AND Wiek IS NOT NULL AND Kurs IS NOT NULL)""")
db7.sql_any_print()

db8 = SqlAlchemyWrite('sqlite:///Pracownicy.db', """SELECT * FROM Pracownicy
WHERE NOT Kurs = "DS" """)
db8.sql_any_print()
