# ============================================================
# 🎬 Netflix Content Analysis using Python & Matplotlib
# ============================================================
# Author: [Your Name]
# Objective:
#   To perform Exploratory Data Analysis (EDA) on Netflix’s dataset
#   and visualize patterns in content type, release trends, ratings,
#   durations, and production countries.
# ============================================================


import os

# Automatically create folder for saving charts
os.makedirs('output_charts', exist_ok=True)



# ------------------------------------------------------------
# 1️⃣ Import Required Libraries
# ------------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt


# ------------------------------------------------------------
# 2️⃣ Load and Clean the Dataset
# ------------------------------------------------------------
# Read the dataset into a pandas DataFrame
df = pd.read_csv('NetFlix.csv')

# Remove any rows with missing values to ensure data integrity
df.dropna(axis=0, inplace=True)


# ------------------------------------------------------------
# 3️⃣ Movies vs TV Shows – Content Type Analysis
# ------------------------------------------------------------
# Count the number of Movies and TV Shows
type_counts = df['type'].value_counts()

# Create a bar chart to compare Movies vs TV Shows
plt.figure(figsize=(6, 4))
plt.bar(type_counts.index, type_counts.values, color=['skyblue', 'orange'])
plt.title('Number of Movies vs TV Shows on Netflix', fontsize=13)
plt.xlabel('Content Type')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('output_charts/Movies_Vs_TvShows.png', dpi=300)
plt.show()


# ------------------------------------------------------------
# 4️⃣ Content Rating Distribution
# ------------------------------------------------------------
# Calculate the frequency of each content rating (e.g., PG, R, TV-MA)
rating_count = df['rating'].value_counts()

# Plot the percentage distribution using a pie chart
plt.figure(figsize=(8, 6))
plt.pie(
    rating_count.values,
    labels=rating_count.index,
    autopct='%1.1f%%',
    startangle=90,
    pctdistance=0.85,
    labeldistance=1.1
)
plt.title('Percentage of Content Ratings on Netflix', fontsize=13)
plt.tight_layout()
plt.savefig('output_charts/content_ratings_pie.png', dpi=300)
plt.show()


# ------------------------------------------------------------
# 5️⃣ Distribution of Movie Durations
# ------------------------------------------------------------
# Filter dataset to include only Movies
movie_df = df[df['type'] == 'Movie'].copy()

# Extract the 'duration' column for histogram plotting
movie_duration = movie_df['duration']

# Visualize how movie durations are distributed
plt.figure(figsize=(8, 6))
plt.hist(movie_duration, bins=30, color='purple', edgecolor='black')
plt.title('Distribution of Movie Durations', fontsize=13)
plt.xlabel('Duration (minutes)')
plt.ylabel('Number of Movies')
plt.tight_layout()
plt.savefig('output_charts/movies_duration_histogram.png', dpi=300, bbox_inches='tight')
plt.show()


# ------------------------------------------------------------
# 6️⃣ Release Trends Over the Years
# ------------------------------------------------------------
# Count total releases per year (Movies + TV Shows)
release_counts = df['release_year'].value_counts().sort_index()

# Scatter plot to show how releases evolved over time
plt.figure(figsize=(10, 6))
plt.scatter(release_counts.index, release_counts.values, color='red', marker='o')
plt.title('Content Releases by Year', fontsize=13)
plt.xlabel('Release Year')
plt.ylabel('Number of Releases')
plt.tight_layout()
plt.savefig('output_charts/release_year_scatter.png', dpi=400, bbox_inches='tight')
plt.show()


# ------------------------------------------------------------
# 7️⃣ Top 10 Content-Producing Countries
# ------------------------------------------------------------
# Identify top 10 countries contributing the most content
country_counts = df['country'].value_counts().head(10)

# Visualize country-wise content volume
plt.figure(figsize=(15, 10))
plt.bar(country_counts.index, country_counts.values, color='teal')
plt.title('Top 10 Countries by Number of Netflix Titles', fontsize=14)
plt.xlabel('Country')
plt.ylabel('Number of Titles')
plt.tight_layout()
plt.savefig('output_charts/top_10_countries.png', dpi=400, bbox_inches='tight')
plt.show()


# ------------------------------------------------------------
# 8️⃣ Movies vs TV Shows by Release Year (Subplot Comparison)
# ------------------------------------------------------------
# Group dataset by release year and content type, then count
content_by_year = df.groupby(['release_year', 'type']).size().unstack().fillna(0)

# Create side-by-side subplots for Movies and TV Shows
fig, ax = plt.subplots(1, 2, figsize=(10, 5))

# Plot movies released per year
ax[0].plot(content_by_year.index, content_by_year['Movie'], color='blue')
ax[0].set_title('Movies Released per Year')
ax[0].set_xlabel('Year')
ax[0].set_ylabel('Number of Movies')

# Plot TV shows released per year
ax[1].plot(content_by_year.index, content_by_year['TV Show'], color='green')
ax[1].set_title('TV Shows Released per Year')
ax[1].set_xlabel('Year')
ax[1].set_ylabel('Number of TV Shows')

# Add a shared title for both subplots
fig.suptitle('Comparison: Movies vs TV Shows Over the Years', fontsize=14)
plt.tight_layout()
plt.savefig('output_charts/movies_tv_shows_comparison.png', dpi=400, bbox_inches='tight')
plt.show()


# ------------------------------------------------------------
# ✅ End of Analysis
# ------------------------------------------------------------
# This project demonstrates Exploratory Data Analysis (EDA) using Matplotlib.
# Insights include:
#   - Netflix hosts more movies than TV shows.
#   - Content production has grown rapidly after 2015.
#   - The US and India are leading contributors.
#   - Most content is rated TV-MA, reflecting adult-oriented content.
#   - Movies typically range between 80–120 minutes in duration.
# ------------------------------------------------------------
