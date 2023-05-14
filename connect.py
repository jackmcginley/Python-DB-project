import sqlite3 as sql # import sqlite3 module

try:
    with sql.connect("filmflix.db") as conn:
        # create a c+onnection object that represent the database
        # connect() methods create a new database if one does not exists. Otherwise use the existing db.
        # create a cursor object to manipulate the db and tables
        cursor = conn.cursor()
except sql.OperationalError as e:
    print(f"Connection Failed!, {e}")
