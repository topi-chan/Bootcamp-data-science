from sa2 import *

db1 = SqlAlchemyCreate('sqlite:///Lista Pracowników.db', "Pracownicy")
db1.sql_create_5col_cstr("id", Integer, "Imię",
String, "Nazwisko", String, "Stanowisko", String, "Dział", String,
)

db2 = SqlAlchemyWrite('sqlite:///Lista Pracowników.db', """INSERT INTO
Pracownicy(id, Imię, Nazwisko, Stanowisko, Dział)
VALUES(:id, :Imię, :Nazwisko, :Stanowisko, :Dział)""")
data = ({ "id": 1, "Imię": "Maciej", "Nazwisko": "Topolewski",
"Stanowisko": "Project Manager", "Dział": "B+R" },
{ "id": 2, "Imię": "Magdalena", "Nazwisko": "Moj",
"Stanowisko": "Asystent", "Dział": "B+R" },
{ "id": 3, "Imię": "Mateusz", "Nazwisko": "Jędryka",
"Stanowisko": "Finansista", "Dział": "Rozliczeń" },
{ "id": 4, "Imię": "Aneta", "Nazwisko": "Woźniak",
"Stanowisko": "Account Manager", "Dział": "Marketing" },
{ "id": 5, "Imię": "Anna", "Nazwisko": "Chmiel",
"Stanowisko": "Specjalista", "Dział": "B+R" })
db2.sql_write(data)


db3 = SqlAlchemyWrite('sqlite:///Lista Pracowników.db', """SELECT * FROM
Pracownicy""")
db3.sql_any_print()

db4 = SqlAlchemyWrite('sqlite:///Lista Pracowników.db', """ALTER TABLE Pracownicy
ADD COLUMN Data_zatrudnienia TEXT DEFAULT 0""")
db4.sql_any()

engine = create_engine('sqlite:///Lista Pracowników.db')
with engine.connect() as con:
    data = { "id": 6, "Imię": "Maciej", "Nazwisko": "Bąk",
    "Stanowisko": "Account Manager", "Dział": "Marketing" }
    statement = text("""INSERT INTO Pracownicy(id, Imię, Nazwisko, Stanowisko, Dział)
    VALUES(:id, :Imię, :Nazwisko, :Stanowisko, :Dział)""")
    con.execute(statement, data)

db5 = SqlAlchemyWrite('sqlite:///Lista Pracowników.db', """SELECT * FROM
Pracownicy""")
db5.sql_any_print()

db6 = SqlAlchemyWrite('sqlite:///Lista Pracowników.db', """UPDATE Pracownicy
SET Data_zatrudnienia = "2020-12-01"
WHERE id = 1""")
db6.sql_any()
db6 = SqlAlchemyWrite('sqlite:///Lista Pracowników.db', """UPDATE Pracownicy
SET Data_zatrudnienia = "2020-12-01"
WHERE id = 2""")
db6.sql_any()
db6 = SqlAlchemyWrite('sqlite:///Lista Pracowników.db', """UPDATE Pracownicy
SET Data_zatrudnienia = "2020-12-01"
WHERE id = 3""")
db6.sql_any()
db6 = SqlAlchemyWrite('sqlite:///Lista Pracowników.db', """UPDATE Pracownicy
SET Data_zatrudnienia = "2020-12-01"
WHERE id = 4""")
db6.sql_any()
db6 = SqlAlchemyWrite('sqlite:///Lista Pracowników.db', """UPDATE Pracownicy
SET Data_zatrudnienia = "2020-12-01"
WHERE id = 5""")
db6.sql_any()
db6 = SqlAlchemyWrite('sqlite:///Lista Pracowników.db', """UPDATE Pracownicy
SET Data_zatrudnienia = "2020-12-01"
WHERE id = 6""")
db6.sql_any()

db7 = SqlAlchemyWrite('sqlite:///Lista Pracowników.db', """SELECT * FROM
Pracownicy""")
db7.sql_any_print()
