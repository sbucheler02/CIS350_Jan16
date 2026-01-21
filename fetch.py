import sqlite3
import pandas as pd

conn = sqlite3.connect('teams.db')

cursor = conn.cursor()

query = """

    SELECT *
    FROM teams;

"""

cursor.execute(query)
records = cursor.fetchall()
conn.close()


lengths = []
for record in records:
    city_len = len(record[1])
    name_len = len(record[2])
    team_lens = (city_len, name_len)
    lengths.append(team_lens)
    

print(lengths)

#records_df = pd.DataFrame(records, columns = ['id', 'city', 'name'])
#print(records_df)