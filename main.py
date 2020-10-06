import mysql.connector
import getpass
import sys
import os

# Name: Library
# Language: Python
# Environment: Visual Studio Code
#
# Author Lukasz Golojuch

mydb = mysql.connector.connect(
host="localhost", #input host
user="root", #input user
password="password", #input password
database="library" #input database
)

def give_back():
    #Function for giving back a book

    os.system('cls' if os.name == 'nt' else 'clear')
    print "-------------------------------"
    print "Give back book: "
    id = input("ID of book you would like to return: ")

    mycursor = mydb.cursor()

    #set borrowed_id as 0 - book isn't borrowed
    sql = "UPDATE books SET borrowed_id = %s WHERE id = %s"
    val = (0, id)

    mycursor.execute(sql, val)

    mydb.commit()

def borrow_book():
    #Function for borrowing book 
    os.system('cls' if os.name == 'nt' else 'clear')
    print "-------------------------------"
    print "Book borrowing system: "
    id = input("What is your your client id: ") #input client id

    mycursor = mydb.cursor()

    #Find customer that id is ...
    sql = "SELECT * FROM customers WHERE id = %s"
    identity = (id, )

    mycursor.execute(sql, identity)    

    myresult = mycursor.fetchall()

    if myresult :
        print "\nHow would you like to find book?"
        print "1. By author" #Find book by author 
        print "2. By book name" #Find book by book name
        answ = input("Your choice: ")

        if answ == 1:
            author = raw_input("Book author: ") #input book author

            #Find all books from this author
            sql = "SELECT * FROM books WHERE author = %s"
            adr = (author, )

            mycursor.execute(sql, adr)

            myresult = mycursor.fetchall()

            print "\n"
            for x in myresult:
                #print all books from this author
                print(x)
            print "\n"

            input_id = input("Input ID of book you want: ")

            sql = "UPDATE books SET borrowed_id = %s WHERE author = %s"
            val = (id, author)

            mycursor.execute(sql, val)

            mydb.commit()

        if answ == 2:
            name = raw_input("Book name: ") #input book name

            #Find all books with this name
            sql = "SELECT * FROM books WHERE name = %s"
            adr = (name, )

            mycursor.execute(sql, adr)

            myresult = mycursor.fetchall()

            print "\n"
            for x in myresult:
                #Find all books with this name
                print(x)
            print "\n"

            input_id = input("Input ID of book you want: ") #ID of book user want to borrow

            #Set borrowed_id as id
            sql = "UPDATE books SET borrowed_id = %s WHERE name = %s"
            val = (id, name)

            mycursor.execute(sql, val)

            mydb.commit()

        else:
            #Wrong input try again
            print "Wrong input..."
            print "Try again"
            borrow_book()

    else:
        #User is not in db... do you want to create new user
        print "Sorry we don't have you in our database"
        print "Do you want to create new account?"
        print("Y/N")
        answ = raw_input()
        if answ == "Y" or answ == "y":
            #create new account
            new_user()
        elif answ == "N" or answ == "n":
            #Turn down program 
            sys.exit("Thank you for using my application")
        else:
            print("Wrong input...")
            borrow_book()


def new_user():
    #Function that create new user
    os.system('cls' if os.name == 'nt' else 'clear')
    print "-------------------------------"
    print "Add new user: "
    name = raw_input("Name: ") #input new user name
    surname = raw_input("Surname: ") #input new user surname
    address = raw_input("Address: ") #input new user address

    mycursor = mydb.cursor()

    #insert new user into customers database
    sql = "INSERT INTO customers (name ,surname ,address) VALUES (%s, %s, %s)"
    val = (name, surname, address)
    mycursor.execute(sql, val)

    mydb.commit()

    print "New user added to library database"
    print "Your ID is:", mycursor.lastrowid #print new user id

def new_book():
    #Function that add new book to database
    os.system('cls' if os.name == 'nt' else 'clear')
    print "-------------------------------"
    print "Add new book: "
    name = raw_input("Name of the book: ") #new book name
    author = raw_input("Author: ") #new book author

    mycursor = mydb.cursor()

    #insert new book into database
    sql = "INSERT INTO books (name, author) VALUES (%s, %s)"
    val = (name, author)
    mycursor.execute(sql, val)

    mydb.commit()

    print "New book added to library database"

def new_worker():
    #Function that add new worker to database
    os.system('cls' if os.name == 'nt' else 'clear')
    print "-------------------------------"
    print "New user"
    username = raw_input("Username: ") #Get username
    password = getpass.getpass(prompt='Password: ') #Get password

    mycursor = mydb.cursor()

    #Insert new worker into login database
    sql = "INSERT INTO login (username, password) VALUES (%s, %s)"
    val = (username, password)
    mycursor.execute(sql, val)

    mydb.commit()

    print "New worker added to database"


def login():
    print "-------------------------------"
    print "Login form"
    #Login Function
    username = raw_input("Username: ") #Get username
    password = getpass.getpass(prompt='Your password: ') #Get password

    mycursor = mydb.cursor()

    sql = "SELECT password FROM login WHERE username = %s" #MySQL order
    adr = (username, )

    mycursor.execute(sql, adr)

    myresult = mycursor.fetchall() 
    
    #return -1 if false else if true
    return str(myresult[0]).find(password) 

def menu():
    #Function that print menu

    print "-------------------------------"
    print "Menu"
    print "1. Borrow a book"
    print "2. Give back a book"
    print "3. Add new user"
    print "4. Add new book"
    print "5. New worker"
    print "6. Exit"
    answ = input("Your choice: ")
    print "-------------------------------"

    if answ == 1:
        #borrow book 
        borrow_book() 
    elif answ == 2:
        #give back a book
        give_back()
    elif answ == 3:
        #add new user to database
        new_user()
    elif answ == 4:
        #add new book to database
        new_book()
    elif answ == 5:
        #add new worker to database
        new_worker()
    elif answ == 6:
        #Exit program
        sys.exit(0)
    else:
        #Wrong input open menu again
        print "Wrong input..."
        print "Try again..."
        menu()
    
    menu()

if __name__ == '__main__':
    print "-------------------------------"
    print "Hello", os.getlogin() #get user login from os
    if login() >= 0:
        #login correct
        print "\nSuccessfull login"
        print "-------------------------------"

        menu()
    else:
        #failed to login 
        print "\nWrong username or password"
        print "Please try again later"
        sys.exit(0)
