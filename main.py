
import sqlite3
from add_record import *
from search_record import *

while True:
    print("Menu for the database\n1) Add New Record\n2) Search a existing record\n3) Exit")
    choice = int(input("Enter your choice : "))

    if 1 == choice:
        print("Adding New Record to Database")
        new_record()
        

    elif 2 == choice:
        print("Searching Database for the existing record")
        search_record()
        

    elif 3 == choice:
        print("Exit")
        break
    else:
        print("Enter the valid option")

