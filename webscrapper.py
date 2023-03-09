import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the URL of the IMDb Top 100 page
url = 'https://www.imdb.com/chart/top/'

# Send a GET request to the URL and get the page content
response = requests.get(url)
page_content = response.text

# Parse the page content using BeautifulSoup
soup = BeautifulSoup(page_content, 'html.parser')

# Find the table that contains the top 100 movies
table = soup.find('table', {'class': 'chart full-width'})

# Find all the rows in the table and loop through them
data = []
rows = table.find_all('tr')[1:]
for row in rows:
    # Find the title of the movie
    title = row.find('td', {'class': 'titleColumn'}).find('a').text.strip()

    # Find the rating of the movie
    rating = row.find('td', {'class': 'ratingColumn imdbRating'}).find('strong').text.strip()

    # Append the data to a list
    data.append([title, rating])

# Create a DataFrame from the data
df = pd.DataFrame(data, columns=['Title', 'Rating'])

# Save the DataFrame to an Excel file
df.to_excel('top_100_movies.xlsx', index=False)
