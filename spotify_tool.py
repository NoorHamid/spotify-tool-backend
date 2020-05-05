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

# print user playlists
sp = spotipy.Spotify(auth=token)
playlists = sp.current_user_playlists(20,0)["items"]
# print(json.dumps(playlist, indent=2))

playlist_names = [x["name"] for x in playlists]
print(playlist_names)

# add tracks to playlist
#print("Number of arguments ", len(sys.argv))
# print("The arguments are: ", str(sys.argv))
print("This is sys.argv: ", sys.argv[0])

if len(sys.argv) > 3:
    username = sys.argv[1]
    playlist_id = sys.argv[2]
    track_ids = sys.argv[3:]
else:
    print("Usage: %s username playlist_id track_id ..." % (sys.argv[0],))
    sys.exit()

scope = 'playlist-modify-public'
token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    results = sp.user_playlist_add_tracks(username, playlist_id, track_ids)
    print(results)
else:
    print("Can't get token for", username)