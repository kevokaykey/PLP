import streamlit as st  # Import Streamlit for building the web app
import pandas as pd  # Import pandas for data manipulation
import matplotlib.pyplot as plt  # Import matplotlib for plotting
from collections import Counter  # Import Counter for word frequency
from wordcloud import WordCloud  # Import WordCloud for word cloud visualization

# Load the dataset
df = pd.read_csv('metadata.csv')  # Read the CSV file into a DataFrame

# Data cleaning and feature engineering
df_clean = df.copy()  # Make a copy to avoid modifying the original data
df_clean['publish_time'] = pd.to_datetime(df_clean['publish_time'], errors='coerce')  # Convert publish_time to datetime
df_clean['publish_year'] = df_clean['publish_time'].dt.year  # Extract year from publish_time
df_clean['abstract_word_count'] = df_clean['abstract'].fillna('').apply(lambda x: len(x.split()))  # Count words in abstract

# Streamlit app layout
st.title("COVID-19 Research Publications Explorer")  # Set the app title
st.write("""
This app allows you to explore COVID-19 research publications by year, journal, and more.
Use the widgets below to filter and visualize the data.
""")  # Add a description

# Sidebar filters for interactivity
years = df_clean['publish_year'].dropna().unique()  # Get unique years
years = sorted([int(y) for y in years if pd.notnull(y)])  # Sort years and ensure they are integers
selected_year = st.sidebar.selectbox("Select Year", options=[None] + years, index=0)  # Dropdown for year selection

journals = df_clean['journal'].dropna().unique()  # Get unique journals
selected_journal = st.sidebar.selectbox("Select Journal", options=[None] + list(journals), index=0)  # Dropdown for journal selection

# Filter data based on user selection
filtered = df_clean.copy()  # Start with the full dataset
if selected_year:
    filtered = filtered[filtered['publish_year'] == selected_year]  # Filter by selected year
if selected_journal:
    filtered = filtered[filtered['journal'] == selected_journal]  # Filter by selected journal

# Show a sample of the filtered data
st.subheader("Sample Data")  # Section header
st.dataframe(filtered.head())  # Display the first few rows of the filtered data

# Publications over time visualization
st.subheader("Number of Publications Over Time")  # Section header
count_papers_by_year = df_clean['publish_year'].value_counts().sort_index()  # Count papers per year
fig1, ax1 = plt.subplots(figsize=(8, 4))  # Create a figure and axis
bars = ax1.bar(count_papers_by_year.index.astype(str), count_papers_by_year.values, color='skyblue', edgecolor='black')  # Bar chart
ax1.set_xlabel('Year')  # X-axis label
ax1.set_ylabel('Number of Papers')  # Y-axis label
ax1.set_title('Publications Over Time')  # Chart title
for bar in bars:
    height = bar.get_height()
    ax1.annotate(f'{int(height)}', xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=8)  # Annotate bars
st.pyplot(fig1)  # Show the plot in Streamlit

# Top journals visualization
st.subheader("Top 10 Journals by Number of Publications")  # Section header
top_journals = df_clean['journal'].value_counts().head(10)  # Get top 10 journals
fig2, ax2 = plt.subplots(figsize=(8, 4))  # Create a figure and axis
top_journals.plot(kind='bar', ax=ax2, color='coral', edgecolor='black')  # Bar chart
ax2.set_xlabel('Journal')  # X-axis label
ax2.set_ylabel('Number of Papers')  # Y-axis label
ax2.set_title('Top 10 Journals')  # Chart title
plt.xticks(rotation=45, ha='right')  # Rotate x labels for readability
st.pyplot(fig2)  # Show the plot in Streamlit

# Word cloud of paper titles
st.subheader("Word Cloud of Paper Titles")  # Section header
title_text = ' '.join(df_clean['title'].dropna())  # Combine all titles into one string
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(title_text)  # Generate word cloud
fig3, ax3 = plt.subplots(figsize=(10, 4))  # Create a figure and axis
ax3.imshow(wordcloud, interpolation='bilinear')  # Show word cloud image
ax3.axis('off')  # Hide axes
st.pyplot(fig3)  # Show the plot in Streamlit

# Distribution by source visualization
st.subheader("Distribution of Paper Counts by Source")  # Section header
source_counts = df_clean['source_x'].value_counts()  # Count papers by source
fig4, ax4 = plt.subplots(figsize=(8, 4))  # Create a figure and axis
source_counts.plot(kind='bar', ax=ax4, color='lightgreen', edgecolor='black')  # Bar chart
ax4.set_xlabel('Source')  # X-axis label
ax4.set_ylabel('Number of Papers')  # Y-axis label
ax4.set_title('Paper Counts by Source')  # Chart title
plt.xticks(rotation=45, ha='right')  # Rotate x labels for readability
plt.tight_layout()  # Adjust layout
st.pyplot(fig4)  # Show the plot in Streamlit