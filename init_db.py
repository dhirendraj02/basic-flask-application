import sqlite3

connection = sqlite3.connect('db.sqlite3')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO meters (id, label) VALUES (?, ?)",
            (1, 'abc')
            )
            
cur.execute("INSERT INTO meters (id, label) VALUES (?, ?)",
            (2, 'xyz')
            )


cur.execute("INSERT INTO meter_data (id, meter_id, value) VALUES (?, ?, ?)",
            (1, 1, 10)
            )

cur.execute("INSERT INTO meter_data (id, meter_id, value) VALUES (?, ?, ?)",
            (2, 1, 20)
            )

cur.execute("INSERT INTO meter_data (id, meter_id, value) VALUES (?, ?, ?)",
            (3, 1, 30)
            )


cur.execute("INSERT INTO meter_data (id, meter_id, value) VALUES (?, ?, ?)",
            (4, 1, 40)
            )


cur.execute("INSERT INTO meter_data (id, meter_id, value) VALUES (?, ?, ?)",
            (5, 2, 50)
            )


connection.commit()
connection.close()

