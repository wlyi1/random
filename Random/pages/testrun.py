import pandas as pd
import sqlite3

# Read sqlite query results into a pandas DataFrame
con = sqlite3.connect("rd1.db")
df = pd.read_sql_query("SELECT * from randomk1", con)

# Verify that result of SQL query is stored in the dataframe
st.write(df.head())

con.close()
