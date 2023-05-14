from connect import *

# subroutines
def allrecords():
    cursor.execute("SELECT * FROM tblfilms") # select all records
    row = cursor.fetchall() # get all the selected records from the table in the db
    for aRecord in row:
        print(aRecord)

def genre():
    filmGenre = input("Entre Genre: ")
    cursor.execute(f"SELECT * FROM tblfilms WHERE Genre = '{filmGenre}' ") # select all records
    row = cursor.fetchall() # get all the selected records from the table in the db
    for aRecord in row:
        print(aRecord)

def year():
    year = input("Enter year released: ")
    cursor.execute(f"SELECT * FROM tblfilms WHERE yearReleased = '{year}' ") # select all records
    row = cursor.fetchall() # get all the selected records from the table in the db
    for aRecord in row:
        print(aRecord)


def rating():
    cert = input("Enter rating: ")
    cursor.execute(f"SELECT * FROM tblfilms WHERE rating = '{cert}' ") # select all records
    row = cursor.fetchall() # get all the selected records from the table in the db
    for aRecord in row:
        print(aRecord)


# if __name__ == "__main__":
#     # call/invoke the function/subroutine
#     allrecords()
#     genre()
#     artists()
#     songID()

