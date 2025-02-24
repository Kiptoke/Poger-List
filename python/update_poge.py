import requests
import os
from dotenv import load_dotenv
from supabase import create_client, Client
from constants import PLAYLISTS, USER_TABLE

def get_bearer():
    params = {
        'grant_type': "client_credentials",
        'client_id': os.getenv('SPOTIFY_CLIENT_ID'),
        'client_secret': os.getenv('SPOTIFY_CLIENT_SECRET')
    }
    headers = {
        'Content-Type': "application/x-www-form-urlencoded"
    }
    bearer = requests.post(
        "https://accounts.spotify.com/api/token",
        params = params,
        headers = headers
    ).json()

    auth = "Bearer " + bearer["access_token"]

    return auth
    
def get_playlist(playlist, bearer):
    endpoint = f'https://api.spotify.com/v1/playlists/{playlist}'
    headers = {
        'Authorization': bearer
    }
    json = requests.get(
        endpoint, 
        headers = headers
    ).json()

    return json

def process_playlist(playlist, playlist_id):
    songs = []
    index = 1

    for s in playlist['tracks']['items']:
        song = s['track']
        artists = []
        stuwant = USER_TABLE[s['added_by']['id']]

        for a in song['artists']:
            artists.append({
                'artistName': a['name'],
                'artistURL': a['external_urls']['spotify']
            })

        songObj = {
            'id': index,
            'songId': song['id'],
            'playlistId': playlist_id,
            'name': song['name'],
            'artists': artists,
            'album': song['album']['name'],
            'albumURL': song['album']['external_urls']['spotify'],
            'length': song['duration_ms'],
            'songURL': song['external_urls']['spotify'],
            'stuwant': stuwant,
            'stuwantURL': s['added_by']['external_urls']['spotify'],
            'poger': playlist['name'],
            'pogerURL': playlist['external_urls']['spotify'],
            'numSongs': playlist['tracks']['total'],
            'dateAdded': s['added_at']
        }
        index += 1
        songs.append(songObj)

    return songs

def publish_playlist(pl):
    url: str = os.getenv('NEXT_PUBLIC_SUPABASE_URL')
    key: str = os.getenv('NEXT_PUBLIC_SUPABASE_ANON_KEY')
    supabase: Client = create_client(url, key)

    response = (
        supabase.table('songs')
        .upsert(pl)
        .execute()
    )

    print(f"{response.data[0]['poger']} ({len(response.data)} songs) processed")

    return
    
if __name__ == "__main__":
    load_dotenv()
    bearer = get_bearer()
    for id in PLAYLISTS:
        pl = get_playlist(id, bearer)
        songs = process_playlist(pl, id)
        publish_playlist(songs)
