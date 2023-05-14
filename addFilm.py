from connect import *
from time import sleep
from readFilms import *

#subroutine
def insertFilm():
    # create an empty list
    films = [] #0, 1, 2
    # ask for user input for the films table(filmID, title, yearReleased, rating, duration, genre)
    title = input("Enter Film Title: ")
    yearReleased = int(input("Enter year released: "))
    rating = input("Enter rating : ")
    duration = int(input("Enter duration in minutes: "))
    genre =  input("Enter film Genre: ")

    # append data from user to the films list
    films.append(title)
    films.append(yearReleased)
    films.append(rating)
    films.append(duration)
    films.append(genre)
     
    try:
        cursor.execute("INSERT INTO tblfilms (title, yearReleased, rating, duration, genre) VALUES(?,?,?,?,?)", films)
        conn.commit() # make the change permanent
        print(f"Title {title} added into the films table")
        # read from the database
        sleep(3) # delay the execution of any code that follows for 3 seconds
        readAllFilms() # call/invoke the function/subroutine
    except sql.OperationalError as e: 
        conn.rollback()
        print(f"Record not added to database: {e}")