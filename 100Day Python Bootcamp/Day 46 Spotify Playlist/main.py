import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

billboard_endpoint = "https://www.billboard.com/charts/hot-100/"
CLIENT_ID = "21978120adb24b39adc45928553aac38"
CLIENT_KEY = "199bdd83a51d4cd59ab87628466c01e9"
USER_NAME = "Helenbzbz"
user_endpoint = "https://api.spotify.com/v1/me/"

# Take day input
# day_to_travel = input("Which year do you want to travel? Type the dat in this format YYYY-MM-DD: ")

# Request information from the website
response = requests.get(f"{billboard_endpoint}2000-08-12")
song_web = BeautifulSoup(response.text, "html.parser")
song_lists = song_web.find_all(name = "div", class_ = "o-chart-results-list-row-container")
song_names = [song.find(name = "h3").text.strip() for song in song_lists]
# print(song_names)

# Connect to Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_KEY,
                                               redirect_uri="http://example.com",
                                               scope="user-library-read playlist-modify-public",
                                               show_dialog=True,
                                               cache_path="token.txt"))
User_id = "31hxpiuhacl7znghnye5asxqbiua"
response = sp.current_user()['id']
print(response)