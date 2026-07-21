import requests
import os
import json
import pandas as pd
from dotenv import load_dotenv
from constants import USER_TABLE, POGERS_FILENAME

def get_playlist_id(raw_url):    
    url = raw_url.strip().split('/')[-1].split('?')[0]
    
    return url

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
    
    # STEP 0 - If the playlist ID already exists, don't even do anything
    pogers = pd.read_csv(POGERS_FILENAME)
    if (playlist in pogers['id'].values):
        repeat = pogers.loc[pogers['id']==playlist].at[0,'name']
        print(f"{repeat} already has been processed!")
        return
    
    # STEP 1 - Get reponse from Spotify API
    endpoint = f'https://api.spotify.com/v1/playlists/{playlist}'
    headers = {
        'Authorization': bearer
    }
    response = requests.get(
        endpoint, 
        headers = headers
    ).json()
    
    # STEP 2- Sanitize response
    if 'tracks' in response:
        response.pop('tracks')
        
    pl_name = response['name'].replace(' ', '_').replace("'", "")
     
    # STEP 3 - Add to poger.csv
    new_row = pd.DataFrame({
        'id': playlist,                             
        'name': response['name'],                     
        'pl_name': pl_name,                             
        'description': response['description'],              
        'url': response['external_urls']['spotify'],  
        'image_url': response['images'][0]['url']           
    }, index=[0])
    pd.concat([pogers, new_row]).to_csv(POGERS_FILENAME, index=False)
        
    # STEP 4 - Generate playlist data csv


def process_playlist_old(playlist, playlist_id):
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

# STEPS TO RUNNING THIS SCRIPT
# 1. Run venv\Scripts\Activate.ps1 in Powershell
# 2. Run pip install -r requirements.txt
# 3. Run file

if __name__ == "__main__":
    load_dotenv()
    
    print("Please input the URL of the Poger playlist:")
    raw_url = input()
    print('\n')
    
    bearer = get_bearer()
    
    get_playlist(get_playlist_id(raw_url), bearer)
    #for id in PLAYLISTS:
    #    pl = get_playlist(id, bearer)
    #    songs = process_playlist(pl, id)
