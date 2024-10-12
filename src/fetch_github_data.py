import requests
import pandas as pd
from utils import logger

def fetch_github_data(topic, per_page=30, pages=5):
    repositories_data = []
    url = f"https://api.github.com/search/repositories?q={topic}&per_page={per_page}"
    
    logger.info(f"Fetching GitHub data for topic: {topic}")
    
    for page in range(1, pages + 1):
        logger.info(f"Fetching page {page} of {pages}")
        try:
            response = requests.get(url + f"&page={page}", timeout=30)
            response.raise_for_status()  # Raise an exception for bad responses
            data = response.json().get('items', [])
            logger.info(f"Successfully fetched {len(data)} repositories from page {page}")

            for repo in data:
                repositories_data.append({
                    "Repository_Name": repo['name'],
                    "Owner": repo['owner']['login'],
                    "Description": repo['description'],
                    "URL": repo['html_url'],
                    "Programming_Language": repo.get('language'),
                    "Creation_Date": repo['created_at'],
                    "Last_Updated_Date": repo['updated_at'],
                    "Number_of_Stars": repo['stargazers_count'],
                    "Number_of_Forks": repo['forks_count'],
                    "Number_of_Open_Issues": repo['open_issues_count'],
                    "License_Type": repo['license']['name'] if repo['license'] else None
                })

        except requests.exceptions.HTTPError as http_err:
            logger.error(f"HTTP error occurred while fetching page {page}: {http_err}")
        except requests.exceptions.ConnectionError as conn_err:
            logger.error(f"Connection error occurred while fetching page {page}: {conn_err}")
        except requests.exceptions.Timeout as timeout_err:
            logger.error(f"Timeout error occurred while fetching page {page}: {timeout_err}")
        except requests.exceptions.RequestException as req_err:
            logger.error(f"Request exception occurred while fetching page {page}: {req_err}")
        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
    
    logger.info(f"Total repositories fetched: {len(repositories_data)}")
    
    data = pd.DataFrame(repositories_data)
    logger.info(f"Dataframe created with {len(data)} rows.")
    return data

if __name__ == "__main__":
    data = fetch_github_data("machine learning")
    print(data.head())
