
from readFilms import *
from addFilm import *
from updateFilm import *
from deleteFilm import *
import reports

"dbMenu"
# create function 
def menuOptions():
    option = 0 # local variable with a value 0
    # while 0 not in ["1","2","3","4","5","6"]:
    while option not in ["1","2","3","4", "5","6"]:
        print("Database Options\n\n1. Add a record.\n2. Delete a record.\n3. Amend a record.\n4. Print all records. \n5. Reports. \n6. Exit")
        #re-assign the value of the options variable
        option = input("Enter an option from the Menu choices above: ") # default datatype for input is string
        if option not in ["1","2","3","4", "5", "6"]:
            print(f"{option} not a in Valid Table choice from Database!")
    return option

"Report Menu"
def reportOptionsMenu():
    options = 0 # local variable with a value 0
    # while 0 not in ["1","2","3","4","5","6"]:
    while options not in ["1","2","3","4","5"]:
        print("Report Menu Options\nEnter to Print By\n1. Details of all films.\n2. All films of a particular genre.\n3. All films of a particular year.\n4. All films of a particular  rating.\n5. To Exit Reports Menu")
        #re-assign the value of the options variable
        options = input("Enter an option from the Report Menu choices above: ") # defualt datatype for input is string
        if options not in ["1","2","3","4","5"]:
            print(f"{options} not a valid choice!")
    return options

# crud operations on database
def films(mainMenu):

    if mainMenu == "1":
        insertFilm() # call the add function from the addFilm.py file/application
    elif mainMenu == "2":
        delete()
    elif mainMenu == "3":
        update()
    elif mainMenu == "4":
        readAllFilms()
    
            
# Reports menu
def showReports():
    reportProgram = True
    print("\n\n")
    while reportProgram:
        reportMenu = reportOptionsMenu()
        if reportMenu == "1":
            # reports.allrecords()
            readAllFilms()
        elif reportMenu == "2":
            reports.genre()
        elif reportMenu == "3":
            reports.year()
        elif reportMenu == "4":
            reports.rating()
        else:
            reportProgram = False
            print("\nReturning to main menu")



# if __name__== "__main__":
#     films()


"Main Program"
filmsDatabase = True # assign mainProgram a variabe True of data type boolean
# while True 
while filmsDatabase:
    filmsDBMenu = menuOptions()
    if filmsDBMenu in ["1","2","3","4"]:
        films(filmsDBMenu)
    elif filmsDBMenu =="5":
        showReports()
    else:
        filmsDatabase = False
input("Press enter to exit the program: ")


