import pandas as pd
import glob
import os
from utils import logger

def concatenate_csv_files(path_pattern):
    """
    Concatenates multiple CSV files into a single DataFrame based on a given path pattern.

    Parameters
    ----------
    path_pattern : str
        The path pattern to search for CSV files.

    Returns
    -------
    pd.DataFrame
        The concatenated DataFrame if successful, otherwise an empty DataFrame.
    """
    try:
        logger.info(f"Looking for CSV files with pattern: {path_pattern}")
        csv_files = glob.glob(path_pattern)
        
        if not csv_files:
            logger.warning(f"No CSV files found for the pattern: {path_pattern}")
            return pd.DataFrame()  # Return an empty DataFrame if no files found
        
        logger.info(f"Found {len(csv_files)} CSV files. Starting concatenation...")

        # Read and concatenate the CSV files
        concatenated_df = pd.concat([pd.read_csv(file, index_col=None) for file in csv_files], ignore_index=True)
        
        logger.info(f"Concatenation successfull. Shape of the concatenated dataframe: {concatenated_df.shape}")
        return concatenated_df
    
    except pd.errors.EmptyDataError as empty_data_err:
        logger.error(f"Empty data error occurred: {empty_data_err}")
    except FileNotFoundError as fnf_error:
        logger.error(f"File not found error: {fnf_error}")
    except Exception as e:
        logger.error(f"An unexpected error occurred during concatenation: {e}")
    
    return pd.DataFrame()  # Return an empty DataFrame in case of errors

if __name__ == "__main__":
    try:
        data = concatenate_csv_files(os.path.join("data", "*.csv"))
        
        if not data.empty:
            output_path = os.path.join("data", "data.csv")
            data.to_csv(output_path, index=False)
            logger.info(f"Concatenated data saved successfully at: {output_path}")
        else:
            logger.warning("No data to save as the concatenated DataFrame is empty.")
    
    except Exception as e:
        logger.error(f"An unexpected error occurred in the main block: {e}")
