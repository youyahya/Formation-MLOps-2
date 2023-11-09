import pandas as pd
import sqlite3
con = sqlite3.connect("mlflow.db")
df = pd.read_sql_query("SELECT * FROM experiments", con)
display(df)
df = pd.read_sql_query("SELECT * FROM metrics", con)
display(df)
sql_query = """SELECT name FROM sqlite_master  
  WHERE type='table';"""
df = pd.read_sql_query(sql_query, con)
display(df)