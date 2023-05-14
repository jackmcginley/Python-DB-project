from connect import *

def readAllFilms():
    try:
        cursor.execute("SELECT * FROM tblfilms") # select all records
        row = cursor.fetchall() # get all the selected records from the table in the db
        for aRecord in row:
            print(aRecord)
    except sql.OperationalError as e: 
        print(f"Records not found: {e}")

def readFilm(recordID):
    try:
        cursor.execute(f"SELECT * FROM tblfilms WHERE filmID = {recordID} ") # select a record
        row = cursor.fetchall() # get all the selected records from the table in the db
        for aRecord in row:
            print(aRecord)
    except sql.OperationalError as e: 
        print(f"Records not found: {e}")


if __name__ == "__main__":
        read() # call/invoke the function/subroutine