from fileinput import close

from flask import Flask, render_template
import sqlite3 as sq

con = sq.connect("flowers.db")
curs = con.cursor()
sqls = """ CREATE TABLE IF NOT EXISTS flower
   (Name TEXT, Flower_in TEXT, Cost INTEGER, State TEXT)"""
sql_insert = """ INSERT INTO 'flower' ( 'Name', 'Flower_in', 'Cost', 'State') VALUES
   ('Петров Виктор Иванович', 'Розы', 5500, 'не куплен'),
   ('Иванов Павел Иванович', 'Тюльпаны', 2500, 'куплен'),
   ('Савченко Нина Николаевна', 'Астры', 3500, 'не куплен'),
   ('Кипоров Алексей Александрович', 'Георгины', 4500, 'куплен'),
   ('Панферова Ася Юрьевна', 'Ромашки', 1300, 'куплен'),
   ('Артюхин Игорь Павлович', 'Ирисы', 7500, 'куплен'),
   ('Вавилов Илья Сергеевич', 'Герберы', 6500, 'не куплен'),
   ('Алехина Арина Радионовна', 'Гибискус', 3300, 'не куплен'),
   ('Орлов Павел Петрович', 'Розы', 8500, 'не куплен'),
   ('Марков Станислав Олегович', 'Гипсофилы', 4500, 'куплен'),
   ('Крюкова Ольга Петровна', 'Тюльпаны', 6500, 'не куплен');"""

curs.execute(sqls)
curs.execute(sql_insert)
con.commit()
con.close()


app = Flask(__name__)


@app.route('/')
def home():
    conn = sq.connect('flowers.db')
    try:
        # connect to the example.db database

        # create a cursor object to execute SQL commands
        c = conn.cursor()
        # execute a SQL command
        c.execute('SELECT * FROM flower')
        # retrieve all the data from the users table

        # close the database connection
        # render the index.html template

        return render_template('index.html', values = c.fetchall())
    finally:
        conn = close()

if __name__ == '__main__':
    app.run(host = "0.0.0.0")
