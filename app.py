import sys
import json
import spotipy
import dotenv
dotenv.load_dotenv()
import spotipy.util as util


SPOTIFY_ACCESS_SCOPE = 'playlist-modify-private'

from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
@app.route('/name/<user>' )
def hello_user(user):
    return f'hello {user}!'

TOKEN = None

@app.before_request
def get_login():
    # Get
    username = request.headers.get('username')
    global TOKEN
    TOKEN = util.prompt_for_user_token(username, SPOTIFY_ACCESS_SCOPE)

    if not TOKEN:
        raise Exception("barf no token")


@app.route('/library', methods=["POST"])
def get_music():
        playlist_ids = request.json['playlist-ids']
        track_ids = request.json['track-ids']
        username = request.json['username']

        # Query playlists
        sp = spotipy.Spotify(auth=token)
        playlists = sp.current_user_playlists(20, 0)["items"]

        # Add tracks to playlist
        sp = spotipy.Spotify(auth=token)
        sp.trace = False
        for playlist in playlist_ids:
            results = sp.user_playlist_add_tracks(username, playlist, track_ids)
            print(results)

        return "lol"

@app.route('/playlists', methods=["GET"])
def list_playlists():
    #Print playlists
    sp = spotipy.Spotify(auth=TOKEN)
    playlists = sp.current_user_playlists(20, 0)["items"]
    names = [{'name': x['name'], 'uri':x['uri']} for x in playlists]
    print(playlists)
    return json.dumps(names)
