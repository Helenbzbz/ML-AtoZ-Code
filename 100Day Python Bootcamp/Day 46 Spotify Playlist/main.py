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
day_to_travel = input("Which year do you want to travel? Type the dat in this format YYYY-MM-DD: ")
song_year = "".join(day_to_travel[0:4])

# Request information from the website
response = requests.get(f"{billboard_endpoint}{day_to_travel}")
song_web = BeautifulSoup(response.text, "html.parser")
song_lists = song_web.find_all(name = "div", class_ = "o-chart-results-list-row-container")
song_names = [song.find(name = "h3").text.strip() for song in song_lists]

# Connect to Spotify
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_KEY,
        show_dialog=True,
        cache_path="100Day Python Bootcamp/Day 46 Spotify Playlist/token.txt"
    )
)
user_id = sp.current_user()['id']

# Search the song url
song_uri_list = []
for name in song_names:
    search_result = sp.search(q = f"track:{name} year:{song_year}", limit = 1, type = "track")
    try:
        uri = (search_result['tracks']['items'][0]['uri'])
    except IndexError:
        pass
    else:
        song_uri_list.append(uri)


# Create Playlist
playlist = sp.user_playlist_create(user=user_id, name=f"{day_to_travel} Billboard 100", public=False)

#Adding songs found into the new playlist
# The function playlist_add_items take a list of uri inputs instead of just one uri
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uri_list)