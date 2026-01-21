import sqlite3

conn = sqlite3.connect('teams.db')

cursor = conn.cursor()

query = """

    INSERT INTO teams(city,name)
    VALUES
    ("Seatle", "Seahawks"),
    ("New England", "Patriots"),
    ("Arizona", "Cardinals"),
    ("Tampa Bay", "Buccaneers"),
    ("Denver", "Broncos"),
    ("Los Angeles", "Rams"),
    ("Buffalo", "Bills"),
    ("Pittsburg", "Steelers");

"""

cursor.execute(query)
conn.commit()
conn.close()