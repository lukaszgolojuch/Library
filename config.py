import mysql.connector
import os
import sys

# Name: Library
# Language: Python
# Environment: Visual Studio Code
#
# Author Lukasz Golojuch

def config():
    
    host_input = raw_input("Host: ")
    user_input = raw_input("User: ")
    password_input = raw_input("Password: ")
    
    #inicialize DB 
    mydb = mysql.connector.connect(
    host=host_input,
    user=user_input,
    password=password_input
    )

    mycursor = mydb.cursor()
    #Create DB named urls 
    mycursor.execute("CREATE DATABASE library")

    #inicialize DB once again with database name
    mydb = mysql.connector.connect(
    host=host_input,
    user=user_input,
    password=password_input,
    database="library"
    )

    mycursor = mydb.cursor()
    #Create table login
    mycursor.execute("CREATE TABLE login(username VARCHAR(50) NOT NULL UNIQUE, password VARCHAR(255) NOT NULL)")
    #Create auto increment primary key as id
    mycursor.execute("ALTER TABLE login ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

    sql = "INSERT INTO login (username, password) VALUES (%s, %s)"
    val = ("root", "password")
    mycursor.execute(sql, val)

    mydb.commit()

    mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255),surname VARCHAR(255), address VARCHAR(255))")
    mycursor.execute("CREATE TABLE books (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255),author VARCHAR(255), borrowed_id INT(4))")

    print("Configuration finished")
    #Now you have to change couple things in main.py
    print("--------------------------------")
    print("Now go to main.py and change: ")
    print("host = ", host_input)
    print("user = ", user_input)
    print("password = ", password_input)
    print("database = library")
    print("--------------------------------")
    print("Application login: ")
    print("Username: root")
    print("Password: password")
    print("--------------------------------")
    print("Now you can use main application")
    sys.exit("Good job!!")

def main():
    print("================================")
    print("Do you want to config your DB?")
    print("Y/N")
    answ = raw_input()
    if answ == "Y" or answ == "y":
        #START configuration
        config()
    elif answ == "N" or answ == "n":
        #Turn down program 
        sys.exit("Thank you for using my application")
    else:
        print("Wrong input...")
        main()

if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Hello ") + os.getlogin()
    main()