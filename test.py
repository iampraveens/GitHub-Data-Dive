import streamlit as st
import pandas as pd 
import os
import sqlite3

db_path = os.path.join("database", "github_data.db")
connection = sqlite3.connect(db_path)

query = """
    SELECT Repository_Name, Last_Updated_Date
    FROM github_repositories
    ORDER BY Last_Updated_Date DESC
    LIMIT 10;
"""
top_repositories = pd.read_sql(query, connection)
top_repo = pd.DataFrame(top_repositories).reset_index(drop=True)
top_repo.index += 1
st.dataframe(top_repo)