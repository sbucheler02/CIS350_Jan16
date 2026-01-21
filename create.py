import sqlite3

conn = sqlite3.connect('teams.db') # .connect(Name of the data base)

cursor = conn.cursor()

query = """

CREATE TABLE IF NOT EXISTS teams(
    id INTEGER PRIMARY KEY,
    city   TEXT,
    name   TEXT
);

"""

cursor.execute(query)
conn.commit()
conn.close()