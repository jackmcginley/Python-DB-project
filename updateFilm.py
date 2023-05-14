from connect import *
from time import sleep
from readFilms import *

def update():
    # which field can be use to update a table(songs)?
    idField = input("Enter the filmID of the record to be updated: ")
    readFilm(idField)
    #field name to be updated
    fieldName = input("Enter the field name (title, yearReleased, rating, duration, genre): ")

    newFieldValue = input(f"Enter the value for {fieldName} field: ")
    # print(newFieldValue)
    newFieldValue = "'"+ newFieldValue+"'"
    print(newFieldValue)

    try:
        # update a specific record
        #UPDATE songs SET Title, Artist, Genre = TitleValue, ArtistValue, Genre/value WHERE SongID = 1,2,3,4....
        cursor.execute(f"UPDATE tblfilms SET {fieldName} = {newFieldValue} WHERE filmID = {idField}")
        "method 2"
        # cursor.execute("UPDATE songs SET " + fieldName + "=" + newFieldValue + "WHERE songID = " + idField )
        conn.commit()

        print(f"Record {idField} updated in the table")
        # read from the database
        sleep(3) # delay the execution of any code that follows for 3 seconds
        readFilm(idField) # call/invoke the function/subroutine
    except sql.OperationalError as e:
        conn.rollback()
        print(f"Record not Updated: {e}")

if __name__ == "__main__":
    update()
