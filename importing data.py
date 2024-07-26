import pandas as pd
import sqlite3

conn=sqlite3.connect("census.db")
curosr=conn.cursor()

df = pd.read_excel("adult_data.xlsx")

df.to_sql('census_data', conn, if_exists='replace', index=False)

conn.commit()