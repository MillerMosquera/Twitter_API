import mysql.connector
from sqlalchemy import create_engine

mysqldb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='0104',
    port=3306,
    database='BIG_DATA'
)
engine = create_engine(
    f'mysql+mysqlconnector://{mysqldb.user}:0104@localhost/BIG_DATA')
# print(engine)
# print(mysqldb)

#mycursor = mysqldb.cursor()

# mycursor.execute("CRUD")
