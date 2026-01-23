import gradio as gr
import sqlite3
import pandas as pd

def fetch_points():
    conn = sqlite3.connect('teams.db')
    cursor = conn.cursor()
    query = """
        SELECT *
        FROM teams;
    """
    cursor.execute(query)
    records = cursor.fetchall()
    conn.close()
    records_df = pd.DataFrame(records, columns = ['id', 'city', 'name'])
    return records_df

iface = gr.Interface(fn = fetch_points, inputs = [], outputs = gr.Dataframe(headers = ['id', 'city', 'name']))

iface.launch()