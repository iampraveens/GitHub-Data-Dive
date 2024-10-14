import streamlit as st
from data_analysis import *
from data_visualization import *

# Streamlit page configuration
st.set_page_config(page_title="GitHub Data Dive", layout="wide")

# Title of the Streamlit app
st.title("GitHub Data Dive: GitHub Repository Insights")

# Dropdown for selecting the type of analysis and visualization
with st.sidebar:
    analysis_type = st.selectbox(
        "Select the type of analysis:",
        [
            "Most Starred Repositories",
            "Most Forked Repositories",
            "Most Recently Updated Repositories",
            "Most Popular Programming Languages",
            "Most Popular Licenses",
            "Most Popular Contributors",
            "Average Stars by Language",
            "Average Forks by Language",
            "Repositories with Open Issues",
            "Repositories Created Each Year",
            "Most Recently Updated Repo",
            "Distribution of Licenses",
            "Most Popular Repository for Each Language"
        ]
    )

data_analysis, empty_column, data_visualization = st.columns([55,4,85])

with data_analysis:
    st.subheader("Data Analysis")


    if analysis_type == "Most Starred Repositories":
        st.markdown("**Top 10 Most Starred Repositories**")
        st.dataframe(most_starred_repositories())
    elif analysis_type == "Most Forked Repositories":
        st.markdown("**Top 10 Most Forked Repositories**")
        st.dataframe(most_forked_repositories())
    elif analysis_type == "Most Recently Updated Repositories":
        st.markdown("**Top 10 Most Recently Updated Repositories**")
        st.dataframe(most_updated_repositories())
    elif analysis_type == "Most Popular Programming Languages":
        st.markdown("**Top 10 Most Popular Programming Languages**")
        st.dataframe(most_popular_languages())
    elif analysis_type == "Most Popular Licenses":
        st.markdown("**Top 10 Most Popular Licenses**")
        st.dataframe(most_popular_licenses())
    elif analysis_type == "Most Popular Contributors":
        st.markdown("**Top 10 Most Popular Contributors**")
        st.dataframe(most_popular_contributors())
    elif analysis_type == "Average Stars by Language":
        st.markdown("**Average Stars by Programming Language**")
        st.dataframe(average_stars_by_language())
    elif analysis_type == "Average Forks by Language":
        st.markdown("**Average Forks by Programming Language**")
        st.dataframe(average_forks_by_language())
    elif analysis_type == "Repositories with Open Issues":
        st.markdown("**Top 10 Repositories with Open Issues**")
        st.dataframe(repos_with_OpenIssues())
    elif analysis_type == "Repositories Created Each Year":
        st.markdown("**Repositories Created Each Year**")
        st.dataframe(repo_created_each_year())
    elif analysis_type == "Most Recently Updated Repo":
        st.markdown("**Most Recently Updated Repo**")
        st.dataframe(most_recently_updated_repo())
    elif analysis_type == "Distribution of Licenses":
        st.markdown("**Distribution of Licenses**")
        st.dataframe(distribution_of_licenses())
    elif analysis_type == "Most Popular Repository for Each Language":
        st.markdown("**Most Popular Repository for Each Language**")
        st.dataframe(popular_repo_for_each_language())

with data_visualization:
    st.subheader("Data Visualization")

    if analysis_type == "Most Starred Repositories":
        most_starred_repositories_visualized()
    elif analysis_type == "Most Forked Repositories":
        most_forked_repositories_visualized()
    elif analysis_type == "Most Recently Updated Repositories":
        most_updated_repositories_visualized()
    elif analysis_type == "Most Popular Programming Languages":
        most_popular_languages_visualized()
    elif analysis_type == "Most Popular Licenses":
        most_popular_licenses_visualized()
    elif analysis_type == "Most Popular Contributors":
        most_popular_contributors_visualized()
    elif analysis_type == "Average Stars by Language":
        average_stars_by_language_visualized()
    elif analysis_type == "Average Forks by Language":
        average_forks_by_language_visualized()
    elif analysis_type == "Repositories with Open Issues":
        repos_with_open_issues_visualized()
    elif analysis_type == "Repositories Created Each Year":
        repo_created_each_year_visualized()
    elif analysis_type == "Most Recently Updated Repo":
        most_recently_updated_repo_visualized()
    elif analysis_type == "Distribution of Licenses":
        distribution_of_licenses_visualized()
    elif analysis_type == "Most Popular Repository for Each Language":
        popular_repo_for_each_language_visualized()
