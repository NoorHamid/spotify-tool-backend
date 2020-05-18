import sys
import spotipy
import spotipy.util as util
import argparse
import dotenv
dotenv.load_dotenv()

# Global variable(s)
# include scopes for both public and private??
SPOTIFY_ACCESS_SCOPE = 'playlist-modify-private'


def parse_args():
    parser = argparse.ArgumentParser(description='This spotify add will add a song to a user playlist or multiple playlists')

    parser.add_argument('--username', '-u', required=True, type=str,
                        help='x')
    parser.add_argument('--playlist_ids', '-p', required=True, type=str,
                        help='x', action = 'append')
    parser.add_argument('--track_ids', '-t', metavar='STR', required=True, type=str,
                        help='x', action = 'append')
    args = parser.parse_args()
    return args

#-- name -x = shorthand name
#metavar = variable.
#req = need config file if true
#type = Path what converts cmd line into.




def main():
    args = parse_args()
    username = args.username
    playlist_ids = args.playlist_ids
    track_ids = args.track_ids

    # Get token
    token = util.prompt_for_user_token(username, SPOTIFY_ACCESS_SCOPE)

    # Query playlists
    playlists = None
    sp = None
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
        #sp.trace = False
        for playlist in playlist_ids:
            results = sp.user_playlist_add_tracks(username, playlist, track_ids)
            print(results)

    else:
        print("Can't get token for", username)

if __name__ == '__main__':
    main()



