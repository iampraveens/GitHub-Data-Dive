import plotly.express as px
import streamlit as st
from data_analysis import *

def most_starred_repositories_visualized():
    top_repo = most_starred_repositories()
    
    fig = px.bar(data_frame=top_repo, x='Number_of_Stars', y='Repository_Name', 
                 orientation='h', title='Top 10 Most Starred Repositories', 
                 color='Number_of_Stars', color_continuous_scale='viridis')
    
    return st.plotly_chart(fig)

def most_forked_repositories_visualized():
    top_repo = most_forked_repositories()
    
    fig = px.bar(data_frame=top_repo, x='Number_of_Forks', y='Repository_Name', 
                 orientation='h', title='Top 10 Most Forked Repositories', 
                 color='Number_of_Forks', color_continuous_scale='earth')
    
    return st.plotly_chart(fig)

def most_updated_repositories_visualized():
    # Get data
    top_repo = most_updated_repositories()
    
    # Convert 'Last_Updated_Date' to datetime
    top_repo['Last_Updated_Date'] = pd.to_datetime(top_repo['Last_Updated_Date'])
    
    # Create the scatter plot without 'size', just using color
    fig = px.scatter(data_frame=top_repo, x='Last_Updated_Date', y='Repository_Name', 
                     title='Top 10 Most Recently Updated Repositories', 
                     color='Last_Updated_Date', color_continuous_scale='plasma',
                     hover_name='Repository_Name')
    
    fig.update_layout(xaxis_title='Last Updated Date', yaxis_title='Repository Name')
    
    # Display the plot in Streamlit
    return st.plotly_chart(fig)

def most_popular_languages_visualized():
    top_lang = most_popular_languages()
    
    fig = px.pie(data_frame=top_lang, values='Count', names='Programming_Language', 
                 title='Top 10 Most Popular Programming Languages', 
                 color_discrete_sequence=px.colors.carto.Tropic)
    
    return st.plotly_chart(fig)

def most_popular_licenses_visualized():
    top_lic = most_popular_licenses()
    
    fig = px.sunburst(data_frame=top_lic, path=['License_Type'], values='Count', 
                      title='Distribution of Top 10 Most Popular Licenses', 
                      color='Count', color_continuous_scale='mint')
    
    return st.plotly_chart(fig)

def most_popular_contributors_visualized():
    top_contrib = most_popular_contributors()
    
    fig = px.bar(data_frame=top_contrib, x='Count', y='Owner', orientation='h', 
                 title='Top 10 Most Popular Contributors', 
                 color='Count', color_continuous_scale='inferno')
    
    return st.plotly_chart(fig)

def average_stars_by_language_visualized():
    top_lang = average_stars_by_language()
    
    fig = px.box(data_frame=top_lang, x='Programming_Language', y='Average_Stars', 
                 title='Average Stars by Programming Language', 
                 color='Programming_Language')
    fig.update_layout(xaxis_title='Programming Language', yaxis_title='Average Stars')
    
    return st.plotly_chart(fig)

def average_forks_by_language_visualized():
    top_lang = average_forks_by_language()
    
    fig = px.box(data_frame=top_lang, x='Programming_Language', y='Average_Forks', 
                 title='Average Forks by Programming Language', 
                 color='Programming_Language')
    fig.update_layout(xaxis_title='Programming Language', yaxis_title='Average Forks')
    
    return st.plotly_chart(fig)

def repos_with_open_issues_visualized():
    top_repo = repos_with_OpenIssues()
    
    fig = px.treemap(data_frame=top_repo, path=['Repository_Name'], values='Number_of_Open_Issues', 
                     title='Top 10 Repositories with Open Issues', 
                     color='Number_of_Open_Issues', color_continuous_scale='reds')
    
    return st.plotly_chart(fig)

def repo_created_each_year_visualized():
    top_repo = repo_created_each_year()
    
    fig = px.line(data_frame=top_repo, x='year', y='count', title='Repositories Created Each Year', 
                  markers=True)
    fig.update_layout(xaxis_title='Year', yaxis_title='Repository Count')
    
    return st.plotly_chart(fig)

def most_recently_updated_repo_visualized():
    top_repo = most_recently_updated_repo()
    
    # Convert 'Last_Updated_Date' to datetime
    top_repo['Last_Updated_Date'] = pd.to_datetime(top_repo['Last_Updated_Date'])
    
    # Create the scatter plot without 'size', just using color
    fig = px.scatter(data_frame=top_repo, x='Last_Updated_Date', y='Repository_Name', 
                     title='Most Recently Updated Repositories', 
                     color='Last_Updated_Date', color_continuous_scale='plasma',
                     hover_name='Repository_Name')
    
    fig.update_layout(xaxis_title='Last Updated Date', yaxis_title='Repository Name')
    
    return st.plotly_chart(fig)

def distribution_of_licenses_visualized():
    top_lic = distribution_of_licenses()
    
    fig = px.pie(data_frame=top_lic, values='Count', names='License_Type', 
                 title='Distribution of Licenses', 
                 hole=0.3, color_discrete_sequence=px.colors.sequential.Oranges)
    
    return st.plotly_chart(fig)

def popular_repo_for_each_language_visualized():
    top_repo = popular_repo_for_each_language()
    
    fig = px.scatter(top_repo, x='Programming_Language', y='Repository_Name', 
                     size='max_stars', title='Most Popular Repository for Each Language', 
                     color='max_stars', color_continuous_scale='tealrose', 
                     hover_name='Repository_Name')
    
    return st.plotly_chart(fig)

