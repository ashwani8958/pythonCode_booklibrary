"This function will add Record in the database"

import sqlite3
import re



def new_record():

    #Loop to check for valid Book ID
    while True:
        book_id = input("Enter the Book ID :- ")
        try:
            book_id = int(book_id)
            break
        except:
            print("Enter the Valid Book ID!! Book ID should be numberical")

    #Loop to check for valid Title
    while True:
        title = input("Enter the Book title :- ")
        if re.search('''[!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~0-9]''',title):
            print("Invalid!! Please enter the valid Title.")
        else:
            break
            
  
    #Loop to check for valid author
    while True:
        author = input("Enter the Author Name :- ")
        if re.search('''[!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~0-9]''', author):
            print("Invalid!! Please enter the valid Author.")
        else:
            break
        
    #loop to check for valid Price
    while True:
        price = input("Enter the price :- ")
        try:
            price = float(price)
            break
        except:
            print("Enter the Valid price!!")


    #Add record to the Database

    #Create database or connect to existing database
    MyLibrary = sqlite3.connect('Library.db')

    #create a cursor object
    curslibrary = MyLibrary.cursor()

    
    try:
        #create the new table only once if it already exist then it will go to except block
        curslibrary.execute('CREATE TABLE Bookdetails(Book_id INTEGER PRIMARY KEY, Title TEXT(25) NOT NULL, Author TEXT(30) NOT NULL, Price REAL NOT NULL);')

        #add the first add to the database
        curslibrary.execute('INSERT INTO Bookdetails(Book_id, Title, Author, Price) VALUES (?, ?, ?, ?);', (book_id, title, author, price))
        MyLibrary.commit()#commit changes to the database
        
    except:
        #add value after the table
        curslibrary.execute('INSERT INTO Bookdetails(Book_id, Title, Author, Price) VALUES (?, ?, ?, ?);', (book_id, title, author, price))
        MyLibrary.commit()#commit changes to the database



                
                
