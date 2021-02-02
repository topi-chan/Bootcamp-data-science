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
{ "id": 4, "Imię": "Aneta", "Nazwisko": None,
"Wiek": 45, "Kurs": "UX" },
{ "id": 5, "Imię": "Anna", "Nazwisko": "Chmiel",
"Wiek": None, "Kurs": "Java" },
{ "id": 6, "Imię": "Patryk", "Nazwisko": "Zieliński",
"Wiek": None, "Kurs": "Tester" },
{ "id": 7, "Imię": "Anna", "Nazwisko": "Kamiński",
"Wiek": None, "Kurs": "Python" },
{ "id": 8, "Imię": "Magdalena", "Nazwisko": "Szymański",
"Wiek": None, "Kurs": "Frontend" },
{ "id": 9, "Imię": "Mateusz", "Nazwisko": "Dąbrowski",
"Wiek": None, "Kurs": "DS" },
{ "id": 10, "Imię": "Aneta", "Nazwisko": "Kozłowski",
"Wiek": 45, "Kurs": "UX" },
{ "id": 11, "Imię": "Anna", "Nazwisko": "Mazur",
"Wiek": 24, "Kurs": None},
{ "id": 12, "Imię": "Patryk", "Nazwisko": "Lewandowski",
"Wiek": 28, "Kurs": "Tester" },
{ "id": 13, "Imię": "Anna", "Nazwisko": "Nowak",
"Wiek": 32, "Kurs": "Python" },
{ "id": 14, "Imię": "Magdalena", "Nazwisko": "Kowalski",
"Wiek": 27, "Kurs": "Frontend" },
{ "id": 15, "Imię": "Mateusz", "Nazwisko": "Wiśniewski",
"Wiek": 28, "Kurs": None},
{ "id": 16, "Imię": "Aneta", "Nazwisko": "Wójcik",
"Wiek": 45, "Kurs": None},
{ "id": 17, "Imię": "Anna", "Nazwisko": "Jankowski",
"Wiek": 24, "Kurs": None},
{ "id": 18, "Imię": "Patryk", "Nazwisko": "Kowalczyk",
"Wiek": 28, "Kurs": None},
{ "id": 19, "Imię": "Mateusz", "Nazwisko": "Kryca",
"Wiek": 28, "Kurs": None},
{ "id": 20, "Imię": "Aneta", "Nazwisko": "Wojnarz",
"Wiek": 45, "Kurs": None})
db2.sql_write(data)

'''poniżej: nie wiem, czy o to chodzi?'''
db3 = SqlAlchemyWrite('sqlite:///Pracownicy.db', """SELECT DISTINCT Imię
 FROM Pracownicy """)
db3.sql_any_print()

db4 = SqlAlchemyWrite('sqlite:///Pracownicy.db', """SELECT DISTINCT Nazwisko
 FROM Pracownicy """)
db4.sql_any_print()

db5 = SqlAlchemyWrite('sqlite:///Pracownicy.db', """SELECT Kurs
 FROM Pracownicy WHERE Nazwisko = "Kowalczyk" """)
db5.sql_any_print()

db6 = SqlAlchemyWrite('sqlite:///Pracownicy.db', """SELECT *
 FROM Pracownicy WHERE Wiek IS NULL """)
db6.sql_any_print()

db7 = SqlAlchemyWrite('sqlite:///Pracownicy.db', """SELECT Wiek
 FROM Pracownicy WHERE Imię = "Patryk" """)
db7.sql_any_print()

db8 = SqlAlchemyWrite('sqlite:///Pracownicy.db', """ALTER TABLE Pracownicy
RENAME TO Mentorzy""")
db8.sql_any()
