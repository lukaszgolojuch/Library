# Program

    Program Name: Library
    Programming Language: Python/MySQL
    Programming Environment: Visual Studio Code

    Author: Łukasz Gołojuch

## About

    An library application that work with MySQL db. It help to add workers, borrow and give back books, add new books and users to library.

## Usage

        1. For the application to function, the computer must have the MySQL DB database installed and running.
    2. You need to run the configuration file named config.py to prepare MySQL DB to work properly with the application.
    3. We make changes to the source code located in a file called main.py, as described at the end of the program config.py

## Functions

def give_back() - function that is created for giving back books

def borrow_book() - function for inserting info about borrowed books

def new_user() - function that is created to add new users to database

def new_book() - function for adding new books to database

def new_worker() - function for adding new workers to database

def login() - function to login as worker

def menu() - function with menu 

## Modules

main.py - main module that adds more URL links to the database, and also reads data from the database, searching for shortened links for easier searching.

config.py - configuration module that allows you to configure the database for application support. Creates a specific database, along with the creation of appropriate tables in it for the proper functioning of the application.

## Licencja
[Open Source]
