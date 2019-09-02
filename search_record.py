import sqlite3
import re

def search_record():
    book_list = list()
    
    #Connect to existing database
    MyLibrary = sqlite3.connect('Library.db')

    #create a cursor object
    curslibrary = MyLibrary.cursor()

    while True:
        #Loop to check for valid Title
        while True:
            title = input("Enter the Book title to search from record :- ")
            if re.search('''[!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~0-9]''',title):
                print("Invalid!! Please enter the valid Title.")
            else:
                break
        
        sql = "SELECT * FROM Bookdetails WHERE Title = '"+title+"';"
        curslibrary.execute(sql)
        record = curslibrary.fetchone()#fetch only the record which is matched
        if record != None:
            print("\nBook is available")
            print(record)
            book_list.append(record[3])#append price of the book to already existing list

            while True:
                copies = input("\nEnter the no. of copies :- ")
                try:
                    copies = int(copies)
                    break
                except:
                    print("\nPlease enter numberic values only\n")

            book_list.append(copies)#append no of copies to the booklist for the calculation of price
        else:
            print("\nBook that you are searching is not available")

        #prompt user to enter choice if he want to search from other book
        choice = input("Do you want to search for another book!! Y/N :- ")
        if choice == 'y'or choice == 'Y':
            while True:
                if re.search('''[!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~0-9]''',title):
                    print("Invalid!! Please enter the valid Title.")
                else:
                    break

                sql = "SELECT * FROM Bookdetails WHERE Title = '"+title+"';"
                curslibrary.execute(sql)
                record = curslibrary.fetchone()#fetch only the record which is matched
                if record != None:
                    print("\nBook is available")
                    print(record)
                    book_list.append(record[3])#fetch only the record which is matched
                    while True:
                        copies = input("\nEnter the no. of copies :- ")
                        try:
                            copies = int(copies)
                            break
                        except:
                            print("\nPlease enter numberic values only\n")

                    book_list.append(copies)#append price of the book to already existing list
                else:
                    print("\nBook that you are searching is not available")
        else:
            break


    i = 0
    total_price = 0

    while i < len(book_list) - 1:
        total_price = total_price + book_list[i]* book_list[i + 1]
        i = i + 2

    print("\n\nTotal Cost {} Rs.\n\n".format(total_price))

        
