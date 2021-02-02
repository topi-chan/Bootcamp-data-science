from sa2 import *

db1 = SqlAlchemyCreate('sqlite:///Pracownicy.db', "Pracownicy")
db1.sql_create_5col_cstr("id", Integer, "Imię",
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
{ "id": 6, "Imię": "Patryk", "Nazwisko": "Zieliński",
"Wiek": 28, "Kurs": "Tester" },
{ "id": 7, "Imię": "Anna", "Nazwisko": "Kamiński",
"Wiek": 32, "Kurs": "Python" },
{ "id": 8, "Imię": "Magdalena", "Nazwisko": "Szymański",
"Wiek": 27, "Kurs": "Frontend" },
{ "id": 9, "Imię": "Mateusz", "Nazwisko": "Dąbrowski",
"Wiek": 28, "Kurs": "DS" },
{ "id": 10, "Imię": "Aneta", "Nazwisko": "Kozłowski",
"Wiek": 45, "Kurs": "UX" },
{ "id": 11, "Imię": "Anna", "Nazwisko": "Mazur",
"Wiek": 24, "Kurs": "Java" },
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
{ "id": 19, "Imię": "Mateusz", "Nazwisko": "Kryca",
"Wiek": 28, "Kurs": "DS" },
{ "id": 20, "Imię": "Aneta", "Nazwisko": "Wojnarz",
"Wiek": 45, "Kurs": "UX" })
db2.sql_write(data)

db3 = SqlAlchemyWrite('sqlite:///Pracownicy.db', """SELECT *
 FROM Pracownicy WHERE Wiek > 30""")
db3.sql_any_print()

db4 = SqlAlchemyWrite('sqlite:///Pracownicy.db', """SELECT *
 FROM Pracownicy WHERE Wiek < 30""")
db4.sql_any_print()

db5 = SqlAlchemyWrite('sqlite:///Pracownicy.db', """SELECT *
 FROM Pracownicy WHERE Nazwisko LIKE 'K%ki'""")
db5.sql_any_print()

db6 = SqlAlchemyWrite('sqlite:///Pracownicy.db', """ALTER TABLE Pracownicy
RENAME COLUMN id TO nr""")
db6.sql_any()

'''to poniżej - jakaś głupia ta kwerenda, ale nie wiem jak to lepiej zapisać'''
db7 = SqlAlchemyWrite('sqlite:///Pracownicy.db', """SELECT * FROM Pracownicy
WHERE nr IS NULL OR Imię IS NULL OR Nazwisko IS NULL OR Wiek IS NULL OR Kurs IS NULL""")
db7.sql_any_print()

db8 = SqlAlchemyWrite('sqlite:///Pracownicy.db', """SELECT * FROM Pracownicy
WHERE Kurs = "Java" """)
db8.sql_any_print()
