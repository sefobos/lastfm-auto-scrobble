import pylast
import random
import requests
from datetime import datetime, timedelta
import time

api_key = ''"
api_secret = ''
username = ''
password_hash = pylast.md5('+')

network = pylast.LastFMNetwork(api_key = api_key, api_secret = api_secret, username = username, password_hash = password_hash)

artist_name = "add here an artist"
ratelimitw = 60 * 60

def fetch_songs(artist_name):
    url = f"http://ws.audioscrobbler.com/2.0/?method=artist.gettoptracks&artist={artist_name}&api_key={api_key}&format=json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'toptracks' in data:
            return data['toptracks']['track']
    return []

def fetch_album(track_name, artist_name):
    url = f"http://ws.audioscrobbler.com/2.0/?method=track.getinfo&api_key={api_key}&artist={artist_name}&track={track_name}&format=json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'track' in data and 'album' in data['track']:
            return data['track']['album']['title']
    return 'nn'

def scrobble_song(track, artist, album):
    try:
        now = int(time.time())
        network.scrobble(artist = artist, title = track, album = album, timestamp = now)
        print(f"scrobbled: {track} by {artist} from album {album}")
    except pylast.WSError as e:
        if "rate limit exceeded" in str(e):
            print("rate limit exceeded pausing for 1 hour...")
            return False
    return True

def scrobbleee():
    songs = fetch_songs(artist_name)
    while True:
        if not songs:
            print("no songs fetched stopping scrobble")
            break
        song = random.choice(songs)
        track = song['name']
        artist = artist_name
        album = fetch_album(track, artist)
        success = scrobble_song(track, artist, album)
        if not success:
            time.sleep(ratelimitw)
        else:
            continue

scrobbleee()
