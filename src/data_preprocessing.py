import pandas as pd
import os
from utils import logger

def preprocess_github_data(input_csv, output_csv):
    try:
        logger.info(f"Starting preprocessing of data from {input_csv}")

        # Read the input CSV file
        data = pd.read_csv(input_csv)
        logger.info(f"Input file {input_csv} read successfully with {data.shape[0]} rows and {data.shape[1]} columns.")

        # Drop the 'Unnamed: 0' column if it exists
        if 'Unnamed: 0' in data.columns:
            data = data.drop(columns=['Unnamed: 0'])
            logger.info("Dropped 'Unnamed: 0' column.")

        # Convert 'Creation_Date' and 'Last_Updated_Date' to datetime
        data['Creation_Date'] = pd.to_datetime(data['Creation_Date'])
        data['Last_Updated_Date'] = pd.to_datetime(data['Last_Updated_Date'])
        logger.info("Converted 'Creation_Date' and 'Last_Updated_Date' columns to datetime format.")

        # Fill missing values in 'Description' column with default text
        data['Description'] = data['Description'].fillna("No description provided")
        logger.info("Filled missing values in 'Description' column with 'No description provided'.")

        # Fill missing values in 'Programming_Language' with the most common language
        if 'Programming_Language' in data.columns:
            most_common_language = data['Programming_Language'].mode()[0]
            data['Programming_Language'] = data['Programming_Language'].fillna(most_common_language)
            logger.info(f"Filled missing values in 'Programming_Language' column with the most common language: {most_common_language}.")

        # Fill missing values in 'License_Type' with the most common license type
        if 'License_Type' in data.columns:
            most_common_license = data['License_Type'].mode()[0]
            data['License_Type'] = data['License_Type'].fillna(most_common_license)
            logger.info(f"Filled missing values in 'License_Type' column with the most common license type: {most_common_license}.")

        # Save the preprocessed data to a new CSV file
        data.to_csv(output_csv, index=False)
        logger.info(f"Preprocessed data saved to {output_csv} successfully.")
    
    except FileNotFoundError as fnf_error:
        logger.error(f"File not found error: {fnf_error}")
    except pd.errors.EmptyDataError as empty_data_err:
        logger.error(f"Empty data error: {empty_data_err}")
    except Exception as e:
        logger.error(f"An unexpected error occurred during preprocessing: {e}")

if __name__ == "__main__":
    input_file = os.path.join("D:\\New Projects\\GitHub Data Dive\\GitHub-Data-Dive\\data", "data.csv")
    output_file = os.path.join("D:\\New Projects\\GitHub Data Dive\\GitHub-Data-Dive\\data", "cleaned_data.csv")
    preprocess_github_data(input_file, output_file)
