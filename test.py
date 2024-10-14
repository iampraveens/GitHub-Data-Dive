import streamlit as st
import sqlite3
import os
import pandas as pd
from utils import logger

db_path = os.path.join("database", "github_data.db")
connection = sqlite3.connect(db_path)

def sql_db_test():
    # db_path = os.path.join("database", "github_data.db")
    # connection = sqlite3.connect(db_path)
    if connection:
        logger.info("Connected to SQLite")
        st.success("Connected to SQLite")
    else:
        logger.error("Failed to connect to SQLite")
        st.error("Failed to connect to SQLite")

    query = "SELECT * FROM github_repositories;"
    try:
        logger.info("Querying most starred repositories...")
        top_repositories = pd.read_sql(query, connection)
        top_repositories.index = top_repositories.index + 1
        logger.info(f"Retrieved {top_repositories.shape[0]} most starred repositories.")
        return top_repositories
    except Exception as e:
        logger.error(f"Error fetching most starred repositories: {e}")
        return pd.DataFrame()
    
def another_analysis():
    # db_path = os.path.join("database", "github_data.db")
    # connection = sqlite3.connect(db_path)
    query = """
        SELECT Repository_Name, Owner, Number_of_Stars
        FROM github_repositories
        ORDER BY Number_of_Stars DESC
        LIMIT 10;
    """
    try:
        logger.info("Querying another analysis...")
        results = pd.read_sql(query, connection)
        results.index = results.index + 1
        logger.info(f"Retrieved {results.shape[0]} records from another analysis.")
        return results
    except Exception as e:
        logger.error(f"Error fetching another analysis: {e}")
        return pd.DataFrame()

# Main Streamlit app
st.title("GitHub Data Dive")

analysis_type = st.selectbox("Select Analysis Type", ["Most Starred Repositories", "Another Analysis"])

if analysis_type == "Most Starred Repositories":
    top_repositories = sql_db_test() # Fetch the data
    if not top_repositories.empty:
        st.write("Top 10 Most Starred Repositories:")
        st.dataframe(top_repositories.head(10)) # Display the top 10
    else:
        st.write("No data available.")
elif analysis_type == "Another Analysis":
    test_analysis = another_analysis()
    if not test_analysis.empty:
        st.write("Top 10 Most Starred Repositories:")
        st.dataframe(test_analysis) 
    else:
        st.write("No data available.")
