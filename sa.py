import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy import inspect
from sqlalchemy.sql import text


class SqlAlchemyCreate():
    """Allows to write a simple table; put database type in 'engine'"""

    def __init__(self, engine, table_name):
        self.engine = engine
        self.table_name = table_name

    def sql_create_3col(self, column1, column2, type1, type2):
        metadata = MetaData()
        books = Table(self.table_name, metadata,
          Column('id', Integer, primary_key=True),
          Column(column1, type1),
          Column(column2, type2),
        )
        engine = create_engine(self.engine)
        metadata.create_all(engine)


class SqlAlchemyWrite():

    def __init__(self, engine, command):
        self.engine = engine
        self.command = command

    def sql_write(self, data):
        engine = create_engine(self.engine)
        with engine.connect() as con:
            statement = text(self.command)
            for line in data:
                con.execute(statement, **line)



# db1 = SqlAlchemyCreate('sqlite:///bookstore.db', "Biblioteczka")
#
# db1.sql_create_3col("tytuł", "data zakupu", String, String)

db2 = SqlAlchemyWrite('sqlite:///bookstore.db', """INSERT INTO Biblioteczka(id, tytuł, data zakupu)
 VALUES(:id, :tytuł, :data zakupu)""")

data = ({ "id": 1, "tytuł": "The Hobbit", "data zakupu": "2020-12-01" },
        { "id": 2, "tytuł": "The Silmarillion", "data zakupu": "2020-11-30" },
        { "id": 3, "tytuł": "Wilk Stepowy", "data zakupu": "2020-11-11" })
db2.sql_write(data)







#command = """INSERT INTO book(id, title, primary_author) VALUES(:id, :title, :primary_author)"""

# class SqlAlchemyWrite():
#     """Writes into already created table"""
#
#     def __init__(self, arg):
#         self.arg = arg




#db1.sql_inspect_3col("Biblioteczka", "tytuł", "data zakupu")

    # def sql_inspect_3col(self, table_name, column1, column2):
    #     inspector = inspect(engine)
    #     inspector.get_columns(table_name)
    #     Out[*]:
    #     [{'autoincrement': True,
    #       'default': None,
    #       'name': u'id',
    #       'nullable': False,
    #       'primary_key': 1,
    #       'type': INTEGER()},
    #      {'autoincrement': True,
    #       'default': None,
    #       'name': u column1,
    #       'nullable': True,
    #       'primary_key': 0,
    #       'type': VARCHAR()},
    #      {'autoincrement': True,
    #       'default': None,
    #       'name': u column2,
    #       'nullable': True,
    #       'primary_key': 0,
    #       'type': VARCHAR()}]
    #
