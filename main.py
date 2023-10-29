import sqlite3

rg = sqlite3.connect('objects.db')
cu = rg.cursor()

cu.execute('''CREATE TABLE IF NOT EXISTS tab1(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    surname TEXT,
    age INTEGER);
''')
cu.execute('''INSERT INTO tab1(name,surname,age)VALUES ('Egor','student',23);''')
cu.execute('''INSERT INTO tab1(name,surname,age)VALUES ('Anton','student',25);''')
cu.execute('''INSERT INTO tab1(name,surname,age)VALUES ('Dima','student',28);''')


rg.commit()

cu.execute('''SELECT * From tab1;''')

k=cu.fetchall()
print(k)


