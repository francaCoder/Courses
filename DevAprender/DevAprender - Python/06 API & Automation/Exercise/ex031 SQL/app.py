# SQL - Structure Query Language
# db.sqlite3

import sqlite3

with sqlite3.connect("musicians.db") as connection:
    # Create a connection with database
    sql = connection.cursor()
    sql.execute("create table band(name text, style text, members interger);")
    # Exemple of entering data
    sql.execute("insert into band(name, style, members) values ('Band 1', 'Rock', 3)")
    # Exemple of use data in a sql command of my sql application
    name = str(input("Band's Name: "))
    style = str(input("Band's Style: "))
    members = int(input("How many Members: "))

    sql.execute(f"insert into band values(?,?,?)", [name, style, members])
    # Looks like .format()
    # Saving
    connection.commit()

    # Show in terminal
    bands = sql.execute("select * from band;")
    for band in bands:
        print(band)