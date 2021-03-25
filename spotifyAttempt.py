import spotipy
# from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials

# SET SPOTIPY_REDIRECT_URI = 'http://localhost'

def verify():
    with open("spotifyCreds.txt", "r") as f:
        creds = [s.strip() for s in f.readlines()]
        client_credentials_manager = SpotifyClientCredentials(client_id=creds[0], client_secret=creds[1])
        scope = "user-library-read"
        sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
        return sp, creds[-1]


class Sp:
    def __init__(self):
        v = verify()
        self.sp = v[0]
        self.username = v[1]

    # gets artist's associated genre(s)
    def getArtistGenre(self, artistName: str) -> [str]:
        result = self.sp.search(artistName)
        track = result['tracks']['items'][0]

        artist = self.sp.artist(track["artists"][0]["external_urls"]["spotify"])
        print("artist genres:", artist["genres"])

        album = self.sp.album(track["album"]["external_urls"]["spotify"])
        print("album genres:", album["genres"])
        print("album release-date:", album["release_date"])

    # gets first search result given a string query -> string of URI
    def getSearchResult(self, query: str, amt: int = 1)  -> str:
        returnString = ""
        results = self.sp.search(q= query, limit=amt)
        # print(results)
        # return results[0]["items"]
        print(results['tracks']['items'][0]['uri'])
        # print(results[0]['tracks']['items']['uri'])
        # for i, t in enumerate(results['tracks']['items']):
        #     print (t['uri'])
        #     returnString = t['uri']
        # return returnString

    # TODO Fix create playlist
    # current error:
    # "This request requires user authentication. http status 403, code:-1"
    def create_playlist(self, playlist_name):
        self.sp.user_playlist_create(self.username, name=playlist_name)

    # TODO don't know if this works yet
    def add_to_playlist(self, playlist_id, track_id):
        self.sp.user_playlist_add_tracks(self.username, playlist_id, track_id)

if __name__ == "__main__":
    sp = Sp()
    # test statements
    # uri = sp.getSearchResult("Loser Big Bang")
    # getSearchResult("Loser Big Bang")
    sp.create_playlist("Test")