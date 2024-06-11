import os
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Spotipy Creds
REDIRECT_URL = "http://example.com"
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

# Billboard Scrape Creds
ID = "title-of-a-story"
PATH = "div ul li ul li h3"
PATH_ARTIST = "div ul li ul li h3"

# Ask date as input
date = input("Which date you want to travel to? Type in this format -> YYYY-MM-DD: ")
URL = f"https://www.billboard.com/charts/hot-100/{date}/"
response = requests.get(URL)
website = response.text
soup = BeautifulSoup(website, "html.parser")

# Add top song names in a list
songs = [song.getText().strip() for song in soup.select(PATH)]

# Spotipy setup
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URL,
                                               scope="playlist-modify-private"))
user_id = sp.current_user()["id"]

# Create playlist
playlist_name = f"TimeMachine {date}"
playlist_description = f"This playlist includes top 100 songs from {date}"
playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False, collaborative=False,
                                   description=playlist_description)
playlist_id = playlist["id"]

# Search song IDs
date_year = date.split("-")[0]
date_range = f"1900-{int(date_year) + 1}"

# Add songs to playlist
uri_list = []
unfound = 0
for song in songs:
    searched = sp.search(q=f"track:{song}, year:{date_range} ", type="track", limit=1)
    try:
        track_uri = searched["tracks"]["items"][0]["uri"]
    except IndexError:
        unfound += 1
        pass
    else:
        uri_list.append(track_uri)

if unfound > 0:
    print(f"There are {unfound} tracks not available in Spotify")

sp.playlist_add_items(playlist_id=playlist_id, items=uri_list)
