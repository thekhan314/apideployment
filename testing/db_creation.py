import sqlite3

connection = sqlite3.connect('animals.db')
cursor = connection.cursor()

create_tbl = " CREATE TABLE animals (id int,species text,category text)"

cursor.execute(create_tbl)

connection.commit()
connection.close()