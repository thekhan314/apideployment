import sqlite3

connection = sqlite3.connect('animals.db')
cursor = connection.cursor()

cat = (1,'cat','mammal')

insert_q = "INSERT INTO animals VALUES (?,?,?)"

cursor.execute(insert_q,cat)

connection.commit()
connection.close()