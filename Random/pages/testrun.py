import sqlite3
import streamlit as st
import pandas as pd
import os

st.markdown("# Run Query")
sqlite_dbs = [file for file in os.listdir('.') if file.endswith('.db')]
db_filename = st.selectbox('DB Filename', sqlite_dbs)

query = st.text_area("SQL Query", height=100)
conn = create_connection(db_filename)

submitted = st.button('Run Query')

if submitted:
    try:
        query = conn.execute(query)
        cols = [column[0] for column in query.description]
        results_df= pd.DataFrame.from_records(
            data = query.fetchall(), 
            columns = cols
        )
        st.dataframe(results_df)
    except Exception as e:
        st.write(e)


