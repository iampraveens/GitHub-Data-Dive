import pandas as pd
import os
import sqlite3
from utils import logger

db_path = os.path.join("database", "github_data.db")
connection = sqlite3.connect(db_path)

def most_starred_repositories():
    """
    Retrieves the top 10 most starred repositories from the GitHub database.

    Returns:
        pd.DataFrame: A DataFrame containing the top 10 most starred repositories.
    """
    
    query = """
        SELECT Repository_Name, Owner, Number_of_Stars
        FROM github_repositories
        ORDER BY Number_of_Stars DESC
        LIMIT 10;
    """
    try:
        logger.info("Querying most starred repositories...")
        top_repositories = pd.read_sql(query, connection)
        logger.info(f"Retrieved {top_repositories.shape[0]} most starred repositories.")
        return top_repositories.reset_index(drop=True).assign(Index=lambda x: x.index + 1)
    except Exception as e:
        logger.error(f"Error fetching most starred repositories: {e}")

def most_forked_repositories():
    """
    Retrieves the top 10 most forked repositories from the GitHub database.

    Returns:
        pd.DataFrame: A DataFrame containing the top 10 most forked repositories.
    """
    query = """
        SELECT Repository_Name, Owner, Number_of_Forks
        FROM github_repositories
        ORDER BY Number_of_Forks DESC
        LIMIT 10;
    """
    try:
        logger.info("Querying most forked repositories...")
        top_repositories = pd.read_sql(query, connection)
        logger.info(f"Retrieved {top_repositories.shape[0]} most forked repositories.")
        return top_repositories.reset_index(drop=True).assign(Index=lambda x: x.index + 1)
    except Exception as e:
        logger.error(f"Error fetching most forked repositories: {e}")

def most_updated_repositories():
    """
    Retrieves the top 10 most recently updated repositories from the GitHub database.

    Returns:
        pd.DataFrame: A DataFrame containing the top 10 most recently updated repositories.
    """
    query = """
        SELECT Repository_Name, Owner, Last_Updated_Date
        FROM github_repositories
        ORDER BY Last_Updated_Date DESC
        LIMIT 10;
    """
    try:
        logger.info("Querying most recently updated repositories...")
        top_repositories = pd.read_sql(query, connection)
        logger.info(f"Retrieved {top_repositories.shape[0]} most updated repositories.")
        return top_repositories.reset_index(drop=True).assign(Index=lambda x: x.index + 1)
    except Exception as e:
        logger.error(f"Error fetching most updated repositories: {e}")

def most_popular_languages():
    """
    Retrieves the top 10 most popular programming languages from the GitHub database.

    Returns:
        pd.DataFrame: A DataFrame containing the top 10 most popular programming languages.
    """
    query = """
        SELECT Programming_Language, Count(*) AS Count
        FROM github_repositories
        GROUP BY Programming_Language
        ORDER BY Count DESC
        LIMIT 10;
    """
    try:
        logger.info("Querying most popular programming languages...")
        top_languages = pd.read_sql(query, connection)
        logger.info(f"Retrieved {top_languages.shape[0]} popular programming languages.")
        return top_languages.reset_index(drop=True).assign(Index=lambda x: x.index + 1)
    except Exception as e:
        logger.error(f"Error fetching popular languages: {e}")

def most_popular_licenses():
    """
    Retrieves the top 10 most popular licenses from the GitHub database.

    Returns:
        pd.DataFrame: A DataFrame containing the top 10 most popular licenses.
    """
    query = """
        SELECT License_Type, Count(*) AS Count
        FROM github_repositories
        GROUP BY License_Type
        ORDER BY Count DESC
        LIMIT 10;
    """
    try:
        logger.info("Querying most popular licenses...")
        top_licenses = pd.read_sql(query, connection)
        logger.info(f"Retrieved {top_licenses.shape[0]} popular licenses.")
        return top_licenses.reset_index(drop=True).assign(Index=lambda x: x.index + 1)
    except Exception as e:
        logger.error(f"Error fetching popular licenses: {e}")

def most_popular_contributors():
    """
    Retrieves the top 10 most popular contributors from the GitHub database.

    Returns:
        pd.DataFrame: A DataFrame containing the top 10 most popular contributors.
    """
    query = """
        SELECT Owner, Count(*) AS Count
        FROM github_repositories
        GROUP BY Owner
        ORDER BY Count DESC
        LIMIT 10;
    """
    try:
        logger.info("Querying most popular contributors...")
        top_contributors = pd.read_sql(query, connection)
        logger.info(f"Retrieved {top_contributors.shape[0]} popular contributors.")
        return top_contributors.reset_index(drop=True).assign(Index=lambda x: x.index + 1)
    except Exception as e:
        logger.error(f"Error fetching popular contributors: {e}")

def average_stars_by_language():
    """
    Retrieves the average number of stars for each programming language from the GitHub database.

    Returns:
        pd.DataFrame: A DataFrame containing the average number of stars for each programming language.
    """
    query = """
        SELECT Programming_Language, AVG(Number_of_Stars) AS Average_Stars
        FROM github_repositories
        GROUP BY Programming_Language
        ORDER BY Average_Stars DESC;
    """
    try:
        logger.info("Querying average stars by programming language...")
        top_languages = pd.read_sql(query, connection)
        logger.info(f"Retrieved {top_languages.shape[0]} languages with average stars.")
        return top_languages.reset_index(drop=True).assign(Index=lambda x: x.index + 1)
    except Exception as e:
        logger.error(f"Error fetching average stars by language: {e}")

def average_forks_by_language():
    """
    Retrieves the average number of forks for each programming language from the GitHub database.

    Returns:
        pd.DataFrame: A DataFrame containing the average number of forks for each programming language.
    """
    query = """
        SELECT Programming_Language, AVG(Number_of_Forks) AS Average_Forks
        FROM github_repositories
        GROUP BY Programming_Language
        ORDER BY Average_Forks DESC;
    """
    try:
        logger.info("Querying average forks by programming language...")
        top_languages = pd.read_sql(query, connection)
        logger.info(f"Retrieved {top_languages.shape[0]} languages with average forks.")
        return top_languages.reset_index(drop=True).assign(Index=lambda x: x.index + 1)
    except Exception as e:
        logger.error(f"Error fetching average forks by language: {e}")

def repos_with_OpenIssues():
    """
    Retrieves the top 10 repositories with open issues from the GitHub database.

    Returns:
        pd.DataFrame: A DataFrame containing the top 10 repositories with open issues.
    """
    query = """
        SELECT Repository_Name, Number_of_Open_Issues
        FROM github_repositories
        WHERE Number_of_Open_Issues > 0
        ORDER BY Number_of_Open_Issues DESC
        LIMIT 10;
    """
    try:
        logger.info("Querying repositories with open issues...")
        top_repositories = pd.read_sql(query, connection)
        logger.info(f"Retrieved {top_repositories.shape[0]} repositories with open issues.")
        return top_repositories.reset_index(drop=True).assign(Index=lambda x: x.index + 1)
    except Exception as e:
        logger.error(f"Error fetching repositories with open issues: {e}")

def repo_created_each_year():
    """
    Retrieves the number of repositories created each year from the GitHub database.

    Returns:
        pd.DataFrame: A DataFrame containing the number of repositories created each year.
    """
    query = """
        SELECT strftime('%Y', Creation_Date) AS year, COUNT(*) AS count
        FROM github_repositories
        GROUP BY year
        ORDER BY year DESC;
    """
    try:
        logger.info("Querying number of repositories created each year...")
        top_repositories = pd.read_sql(query, connection)
        logger.info(f"Retrieved {top_repositories.shape[0]} years of repository creation data.")
        return top_repositories.reset_index(drop=True).assign(Index=lambda x: x.index + 1)
    except Exception as e:
        logger.error(f"Error fetching repository creation data by year: {e}")

def most_recently_updated_repo():
    """
    Retrieves the top 10 most recently updated repositories from the GitHub database.

    Returns:
        pd.DataFrame: A DataFrame containing the top 10 most recently updated repositories.
    """
    query = """
        SELECT Repository_Name, Last_Updated_Date
        FROM github_repositories
        ORDER BY Last_Updated_Date DESC
        LIMIT 10;
    """
    try:
        logger.info("Querying most recently updated repositories...")
        top_repositories = pd.read_sql(query, connection)
        logger.info(f"Retrieved {top_repositories.shape[0]} most recently updated repositories.")
        return top_repositories.reset_index(drop=True).assign(Index=lambda x: x.index + 1)
    except Exception as e:
        logger.error(f"Error fetching most recently updated repositories: {e}")

def distribution_of_licenses():
    """
    Retrieves the distribution of licenses from the GitHub database.

    Returns:
        pd.DataFrame: A DataFrame containing the license distribution records.
    """
    query = """
        SELECT License_Type, Count(*) AS Count
        FROM github_repositories
        GROUP BY License_Type
        ORDER BY Count DESC;
    """
    try:
        logger.info("Querying distribution of licenses...")
        top_licenses = pd.read_sql(query, connection)
        logger.info(f"Retrieved {top_licenses.shape[0]} license distribution records.")
        return top_licenses.reset_index(drop=True).assign(Index=lambda x: x.index + 1)
    except Exception as e:
        logger.error(f"Error fetching distribution of licenses: {e}")

def popular_repo_for_each_language():
    """
    Retrieves the most popular repository for each programming language from the GitHub database.

    Returns:
        pd.DataFrame: A DataFrame containing the most popular repository for each programming language.
    """
    query = """
        SELECT Programming_Language, Repository_Name, MAX(Number_of_Stars) AS max_stars
        FROM github_repositories
        GROUP BY Programming_Language
        ORDER BY max_stars DESC;
    """
    try:
        logger.info("Querying most popular repository for each language...")
        top_repositories = pd.read_sql(query, connection)
        logger.info(f"Retrieved {top_repositories.shape[0]} popular repositories for each language.")
        return top_repositories.reset_index(drop=True).assign(Index=lambda x: x.index + 1)
    except Exception as e:
        logger.error(f"Error fetching popular repository for each language: {e}")
