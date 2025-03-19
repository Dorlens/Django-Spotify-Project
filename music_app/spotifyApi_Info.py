from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth


SPOTIPY_CLIENT_ID = '87c117f8d08343dfa2e4bbd630f09b5b'
SPOTIPY_CLIENT_SECRET = '18eff287e1fa46ca947aa06056803d18'


sp = Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri="http://127.0.0.1:8000/random_track/",
        scope="user-modify-playback-state"
    )
)

