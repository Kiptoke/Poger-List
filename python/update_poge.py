import requests
import os
import pandas as pd
from dotenv import load_dotenv
from constants import PLAYLISTS, USER_TABLE, POGERS_FILENAME

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
    print(f"Calling Spotify API on playlist {playlist}...") 
    endpoint = f'https://api.spotify.com/v1/playlists/{playlist}'
    headers = {
        'Authorization': bearer
    }
    try:
        response = requests.get(
            endpoint, 
            headers = headers
        ).json()
    except:
        print("Error calling Spotify Playlists API")
    
    # STEP 2- Sanitize response
    print(f"Read in {response['name']}, beginning poger processing")
    if 'tracks' in response:
        response.pop('tracks')
        
    pl_name = response['name'].replace(' ', '_').replace("'", "")
     
    # STEP 3 - Add to poger.csv
    print(f"Adding {response['name']} to {POGERS_FILENAME}")
    new_row = pd.DataFrame({
        'id': playlist,                             
        'name': response['name'],                     
        'pl_name': pl_name,                             
        'description': response['description'],              
        'url': response['external_urls']['spotify'],  
        'image_url': response['images'][0]['url']           
    }, index=[0])
    try:
        pd.concat([pogers, new_row]).to_csv(POGERS_FILENAME, index=False)
    except:
        print(f"Error adding {response['name']} to {POGERS_FILENAME}")
    print(f"Successfully added {response['name']} to {POGERS_FILENAME}")
        
    # STEP 4 - Setup for CSV of all songs in poger
    print(f"Generating {pl_name}.csv...")
    song = []
    song_url = []
    artist = []
    artist_url = []
    album = []
    album_url = []
    stuwant = []
    stuwant_url = []
    duration = []
    timestamp = []
    
    try:
        for s in response['items']['items']:
            song.append(s['track']['name'])
            song_url.append(s['track']['external_urls']['spotify'])
            artist.append(s['track']['artists'][0]['name'])
            artist_url.append(s['track']['artists'][0]['external_urls']['spotify'])
            album.append(s['track']['album']['name'])
            album_url.append(s['track']['album']['external_urls']['spotify'])
            stuwant.append(s['added_by']['id'])
            stuwant_url.append(s['added_by']['external_urls']['spotify'])
            duration.append(s['track']['duration_ms'])
            timestamp.append(s['added_at'])
    except:
        print(f"Error while reading songs from {response['name']}")
        print({
            'song': song,
            'song_url': song_url,
            'artist': artist,
            'artist_url': artist_url,
            'album': album,
            'album_url': album_url,
            'stuwant': stuwant,
            'stuwant_url': stuwant_url,
            'duration': duration,
            'timestamp': timestamp
        })
        
    # STEP 5 - Add to {poger_name}.csv
    try:
        pd.DataFrame({
            'song': song,
            'song_url': song_url,
            'artist': artist,
            'artist_url': artist_url,
            'album': album,
            'album_url': album_url,
            'stuwant': stuwant,
            'stuwant_url': stuwant_url,
            'duration': duration,
            'timestamp': timestamp
        }).to_csv(f"data/{pl_name}.csv", index=False)
    except:
        print(f"Error while generating {pl_name}.csv")
    print(f"Successfully created {pl_name}.csv")

# STEPS TO RUNNING THIS SCRIPT
# 1. Run venv\Scripts\Activate.ps1 in Powershell
# 2. Run pip install -r requirements.txt
# 3. Run file

if __name__ == "__main__":
    load_dotenv()
    
    print("Processing Poger...")
    print('\n')
    
    bearer = get_bearer()
    
    for url in PLAYLISTS:
        get_playlist(get_playlist_id(url), bearer)

