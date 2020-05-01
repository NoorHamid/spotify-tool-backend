import sys
import spotipy
import spotipy.util as util
import dotenv

dotenv.load_dotenv()

# spotify creds
spotify_user = ""
# include scopes for both public and private??
spotify_access_scope = 'playlist-modify-public'

token = util.prompt_for_user_token(spotify_user, spotify_access_scope)

if token:
    sp = spotipy.Spotify(auth=token)
    all_playlists = []
    playlist = sp.current_user_playlists(20,0)
    all_playlists.append(playlist)

print(all_playlists)



