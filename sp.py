# using authorization code flow
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
# Set environment variables
os.environ["SPOTIPY_CLIENT_ID"] = ""
os.environ["SPOTIPY_CLIENT_SECRET"] = ""
os.environ["SPOTIPY_REDIRECT_URI"] = "http://localhost:8000"
os.environ["SPOTIFY_USERNAME"] = ""
SPOTIFY_USERNAME=""

# define environment variables return sp object
def init():
    global SPOTIFY_USERNAME
    with open("spotifyCreds.txt", "r") as f:
        items = [line.strip() for line in f.readlines()]
        os.environ["SPOTIPY_CLIENT_ID"] = items[0]
        os.environ["SPOTIPY_CLIENT_SECRET"] = items[1]
        # SPOTIFY_USERNAME = items[2]
    # scope = "playlist-modify-public, playlist-modify-private, user-library-read, user-top-read"
    # sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    # return sp
    scope = "playlist-modify-public, playlist-modify-private, user-library-read, user-top-read"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    SPOTIFY_USERNAME = sp.me()['id']
    print(sp.me()['id'])
    return sp

class Sp:
    def __init__(self):
        self.sp = init()

    # takes search query of "title artist"
    # returns: first song's uri
    # TODO - better parse search to run more efficiently
    def getSearchResult(self, query: str, amt: int=1) -> str:
        uri = ""
        print(query)
        result = self.sp.search(q=query, limit=5)
        try: 
            firstTrack = result['tracks']['items'][0]['uri']
            return firstTrack
        except IndexError:
            print("Search invalid")
            
    # creates playlist
    # gets first playlists' id
    # returns: playlist id
    def create_playlist(self, name: str, public: bool="True"):
        self.sp.user_playlist_create(SPOTIFY_USERNAME, name=name)
        playlists = self.sp.current_user_playlists(limit=1, offset=0)
        return playlists["items"][0]["id"]

    # takes playlist id and list of song uris and adds them to playlist
    def add_to_playlist(self, id: str, items: [str]):
        self.sp.playlist_add_items(id, items)

if __name__ == "__main__":
    sp = Sp()
    playlist_id = sp.create_playlist("test1")
    items = ["spotify:track:2vzn8usBcuNL93DnTjEK0z"]
    sp.add_to_playlist(playlist_id, items)