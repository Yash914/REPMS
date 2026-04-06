import pandas as pd
from db import get_connection

def fetch_data(query):
    conn = get_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def execute_query(query, values=None):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, values or ())
    conn.commit()
    conn.close()