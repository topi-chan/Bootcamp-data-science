from sa import *


db1 = SqlAlchemyCreate('sqlite:///bookstore.db', "Biblioteczka")
db1.sql_create_3col("tytuł", "data_zakupu", String, String)

db2 = SqlAlchemyWrite('sqlite:///bookstore.db', """INSERT INTO
Biblioteczka(id, tytuł, data_zakupu) VALUES(:id, :tytuł, :data_zakupu)""")
data = ({ "id": 1, "tytuł": "The Hobbit", "data_zakupu": "2020-12-01" },
        { "id": 2, "tytuł": "The Silmarillion", "data_zakupu": "2020-11-30" },
        { "id": 3, "tytuł": "Wilk Stepowy", "data_zakupu": "2020-11-11" }
        )
db2.sql_write(data)

db3 = SqlAlchemyWrite('sqlite:///bookstore.db', """SELECT tytuł FROM Biblioteczka""")
db3.sql_any_print()

db4 = SqlAlchemyWrite('sqlite:///bookstore.db', """UPDATE Biblioteczka
SET id = 3 WHERE tytuł = "The Hobbit" """)
db4.sql_any()

db5 = SqlAlchemyWrite('sqlite:///bookstore.db', """UPDATE Biblioteczka SET
id = 1 WHERE tytuł = "Wilk Stepowy" """)
db5.sql_any()

db6 = SqlAlchemyWrite('sqlite:///bookstore.db', """ALTER TABLE Biblioteczka
ADD COLUMN autor TEXT""")
db6.sql_any()

db7 = SqlAlchemyWrite('sqlite:///bookstore.db', """UPDATE Biblioteczka SET
autor = "Hermann Hesse" WHERE tytuł = "Wilk Stepowy" """)
db7.sql_any()
db7 = SqlAlchemyWrite('sqlite:///bookstore.db', """UPDATE Biblioteczka SET
autor = "Tolkien" WHERE tytuł = "The Silmarillion" """)
db7.sql_any()
db7 = SqlAlchemyWrite('sqlite:///bookstore.db', """UPDATE Biblioteczka SET
autor = "Tolkien" WHERE tytuł = "The Hobbit" """)
db7.sql_any()

db8 = SqlAlchemyWrite('sqlite:///bookstore.db', """DELETE FROM Biblioteczka
WHERE autor = "Tolkien" """)
db8.sql_any()

db9 = SqlAlchemyWrite('sqlite:///bookstore.db', """SELECT autor FROM Biblioteczka""")
db9.sql_any_print()
