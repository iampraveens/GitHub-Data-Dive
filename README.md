# GitHub Data Dive

GitHub Data Dive is a comprehensive tool for analyzing and visualizing data from GitHub repositories. This project fetches data from the GitHub API, processes it, stores it in a SQLite database, and provides various analyses and visualizations through a Streamlit web application.

## Features

- Fetch repository data from GitHub API
- Process and clean the fetched data
- Store data in a SQLite database
- Perform various analyses on GitHub repositories, including:
  - Most starred repositories
  - Most forked repositories
  - Most recently updated repositories
  - Popular programming languages
  - License distribution
  - Contributor statistics
  - And more!
- Visualize the analyzed data using Plotly
- Interactive web interface using Streamlit

## Project Structure

- `src/`: Source code directory
  - `utils/`: Utility functions and logging setup
  - `fetch_github_data.py`: Script to fetch data from GitHub API
  - `concatenate_csv_files.py`: Script to combine multiple CSV files
  - `data_preprocessing.py`: Data cleaning and preprocessing
  - `push_to_sqlite.py`: Store processed data in SQLite database
  - `data_analysis.py`: Various data analysis functions
  - `data_visualization.py`: Functions for creating visualizations
- `app.py`: Main Streamlit application
- `setup.py`: Project setup file
- `requirements.txt`: List of project dependencies
- `template.py`: Script to set up the initial project structure

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/iampraveens/GitHub-Data-Dive.git
   cd GitHub-Data-Dive
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\\Scripts\\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up your environment variables:
   Create a `.env` file in the root directory and add your GitHub API token:
   ```
   GITHUB_API_TOKEN=your_github_api_token_here
   ```

## Usage

1. Run the data fetching and processing scripts:
   ```
   python src/fetch_github_data.py
   python src/concatenate_csv_files.py
   python src/data_preprocessing.py
   python src/push_to_sqlite.py
   ```

2. Start the Streamlit app:
   ```
   streamlit run app.py
   ```

3. Open your web browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`).

4. Use the sidebar to select different types of analyses and explore the visualizations.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Author

- Praveen S ([@iampraveens](https://github.com/iampraveens))
- Email: praveensivaprakasham@gmail.com

## Acknowledgments

- Thanks to the GitHub API for providing access to repository data.
- This project uses various open-source libraries, including Pandas, SQLAlchemy, Plotly, and Streamlit.