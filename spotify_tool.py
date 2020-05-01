import sys
import spotipy
import spotipy.util as util
import dotenv
import json

dotenv.load_dotenv()

# spotify creds
spotify_user = ""
# include scopes for both public and private??
spotify_access_scope = 'playlist-modify-public'

token = util.prompt_for_user_token(spotify_user, spotify_access_scope)

if not token:
    exit(1)

sp = spotipy.Spotify(auth=token)
playlists = sp.current_user_playlists(20,0)["items"]
# print(json.dumps(playlist, indent=2))

playlist_names = [x["name"] for x in playlists]
print(playlist_names)



