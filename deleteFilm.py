from connect import *
from time import sleep
from readFilms import *

def delete():
    # which field can be use to delete a song in a table(songs)?
    idField = input("Enter the filmID of the record to be deleted: ")
    try:
        cursor.execute(f"DELETE FROM tblfilms WHERE filmID = {idField}")
        # cursor.execute(f"DELETE FROM songs WHERE SongID = >50")
        "Method 2"
        # cursor.execute("DELETE FROM songs WHERE SongID=" + idField)

        conn.commit()

        print(f"Record {idField} deleted from the films table")
        # read from the database
        sleep(3) # delay the execution of any code that follows for 3 seconds
        readAllFilms() # call/invoke the function/subroutine
    except sql.OperationalError as e:
            conn.rollback()
            print(f"Record not found in database: {e}")

if __name__ == "__main__":
    delete()