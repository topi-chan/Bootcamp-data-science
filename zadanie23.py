from sa import *


db1 = SqlAlchemyCreate('sqlite:///School_Coding.db', "Mentors")
db1.sql_create_6col("id", Integer, "Imię", String, "Nazwisko", String,
"Specjalizacja", String, "Data_zatrudnienia", String, "Data_zwolnienia", String)

db2 = SqlAlchemyWrite('sqlite:///School_Coding.db', """INSERT INTO
Mentors(id, Imię, Nazwisko, Specjalizacja, Data_zatrudnienia, Data_zwolnienia)
VALUES(:id, :Imię, :Nazwisko, :Specjalizacja, :Data_zatrudnienia, :Data_zwolnienia)""")
data = ({ "id": 1, "Imię": "Maciej", "Nazwisko": "Karczewski",
"Specjalizacja": "Python", "Data_zatrudnienia": "2020-12-01",
"Data_zwolnienia": "2020-12-13" },
{ "id": 2, "Imię": "Maciej", "Nazwisko": "Karczewski",
"Specjalizacja": "DS", "Data_zatrudnienia": "2020-12-01",
"Data_zwolnienia": "2020-12-13" },
{ "id": 3, "Imię": "Maciej", "Nazwisko": "Karczewski",
"Specjalizacja": "DS", "Data_zatrudnienia": "2020-12-01",
"Data_zwolnienia": "2020-12-13" },
{ "id": 4, "Imię": "Maciej", "Nazwisko": "Karczewski",
"Specjalizacja": "DS", "Data_zatrudnienia": "2020-12-01",
"Data_zwolnienia": "2020-12-13" },
{ "id": 5, "Imię": "Maciej", "Nazwisko": "Karczewski",
"Specjalizacja": "DS", "Data_zatrudnienia": "2020-12-01",
"Data_zwolnienia": "2020-12-13" },
{ "id": 6, "Imię": "Maciej", "Nazwisko": "Karczewski",
"Specjalizacja": "DS", "Data_zatrudnienia": "2020-12-01",
"Data_zwolnienia": "2020-12-13" },
{ "id": 7, "Imię": "Maciej", "Nazwisko": "Karczewski",
"Specjalizacja": "DS", "Data_zatrudnienia": "2020-12-01",
"Data_zwolnienia": "2020-12-13" },
{ "id": 8, "Imię": "Maciej", "Nazwisko": "Karczewski",
"Specjalizacja": "DS", "Data_zatrudnienia": "2020-12-01",
"Data_zwolnienia": "2020-12-13" },
{ "id": 9, "Imię": "Maciej", "Nazwisko": "Karczewski",
"Specjalizacja": "DS", "Data_zatrudnienia": "2020-12-01",
"Data_zwolnienia": "2020-12-13" },
{ "id": 10, "Imię": "Maciej", "Nazwisko": "Karczewski",
"Specjalizacja": "DS", "Data_zatrudnienia": "2020-12-01",
"Data_zwolnienia": "2020-12-13" })
db2.sql_write(data)

db3 = SqlAlchemyWrite('sqlite:///School_Coding.db', """SELECT * FROM Mentors""")
db3.sql_any_print()

db4 = SqlAlchemyWrite('sqlite:///School_Coding.db', """UPDATE Mentors SET
Nazwisko = "Jączewski" WHERE id = 5 """)
db4.sql_any()

db5 = SqlAlchemyWrite('sqlite:///School_Coding.db', """SELECT Nazwisko FROM
Mentors WHERE id = 5 """)
db5.sql_any_print()

db6 = SqlAlchemyWrite('sqlite:///School_Coding.db', """UPDATE Mentors SET
Specjalizacja = "SCRUM" WHERE id = 9 """)
db6.sql_any()

db7 = SqlAlchemyWrite('sqlite:///School_Coding.db', """SELECT Nazwisko FROM
Mentors WHERE id = 9 """)
db7.sql_any_print()

db8 = SqlAlchemyWrite('sqlite:///School_Coding.db', """ALTER TABLE Mentors
ADD COLUMN Wynagrodzenie INTEGER DEFAULT 0""")
db8.sql_any()

db9 = SqlAlchemyWrite('sqlite:///School_Coding.db', """UPDATE Mentors SET
Wynagrodzenie = 1000 WHERE id = 1""")
db9.sql_any()
db9 = SqlAlchemyWrite('sqlite:///School_Coding.db', """UPDATE Mentors SET
Wynagrodzenie = 1000 WHERE id = 2""")
db9.sql_any()
db9 = SqlAlchemyWrite('sqlite:///School_Coding.db', """UPDATE Mentors SET
Wynagrodzenie = 1000 WHERE id = 3""")
db9.sql_any()

db10 = SqlAlchemyWrite('sqlite:///School_Coding.db', """SELECT * FROM
Mentors WHERE id = 1 """)
db10.sql_any_print()
db10 = SqlAlchemyWrite('sqlite:///School_Coding.db', """SELECT * FROM
Mentors WHERE id = 2 """)
db10.sql_any_print()
db10 = SqlAlchemyWrite('sqlite:///School_Coding.db', """SELECT * FROM
Mentors WHERE id = 3 """)
db10.sql_any_print()
