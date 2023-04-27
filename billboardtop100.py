import requests
from bs4 import BeautifulSoup
import re

# URL for the billboard.com chart
url = "https://www.billboard.com/charts/hot-100"

# Send HTTP request to get the web content of the site
response = requests.get(url)

# Create the soup object to parse for data
soup = BeautifulSoup(response.text, "html.parser")

# Construct a list containing all h3 tags with a class name containing c-title a-no-trucate
# This was determined to be common amongst all song names in the list
# Use regex to search for the "c-title..." substring since they're all slightly different
song_container = soup.find_all("h3", {"class" : re.compile('c-title a-no-trucate.*')})

# Make an empty python dictionary for the stripped song names
song_titles = []

# Strip the html from around the song names so we're left with just the names of the songs
# Add the cleaned song titles to the dictionary we created above
for song in song_container:
    song_titles.append(song.text.strip())

# Print the output in the form of: 
# 1. Song Title
# 2. Song Title... 
print("Top songs in North America:")
for i in range(100):
    print(f"{i+1}. {song_titles[i]}")
