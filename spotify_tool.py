import sys
import spotipy
import spotipy.util as util

# Global variable(s)
# include scopes for both public and private??
SPOTIFY_ACCESS_SCOPE = 'playlist-modify-private'

# Get arguments
print("This is sys.argv: ", sys.argv[0])
if len(sys.argv) > 3:
    username = sys.argv[1]
    playlist_id = sys.argv[2]
    track_ids = sys.argv[3:]
else:
    print("Usage: %s username playlist_id track_id ..." % (sys.argv[0],))
    sys.exit()

# Get token
token = util.prompt_for_user_token(username, SPOTIFY_ACCESS_SCOPE)

# Query playlists
playlists = None
if token:
    sp = spotipy.Spotify(auth=token)
    playlists = sp.current_user_playlists(20, 0)["items"]
else:
    print(f"Can't get token for user {username}!")

# Print playlists
if playlists:
    playlist_names = [x["name"] for x in playlists]
    print(playlist_names)
else:
    print('No playlists found!')

# Add tracks to playlist
if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    results = sp.user_playlist_add_tracks(username, playlist_id, track_ids)
    print(results)
else:
    print("Can't get token for", username)