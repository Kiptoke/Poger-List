from pathlib import Path
import datetime
import json
import requests
import client
    
def get_bearer():
    params = {
        'grant_type': "client_credentials",
        'client_id': client.CLIENT_ID,
        'client_secret': client.CLIENT_SECRET
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

def get_playlist(playlist_id, bearer):
    endpoint = f'https://api.spotify.com/v1/playlists/{playlist_id}'
    headers = {
        'Authorization': bearer
    }
    pl = requests.get(
        endpoint, 
        headers = headers
    ).json()
    
    return pl

def get_melody():
    # "65rLedogOjLqWp938fZCNu", melody is poger - requires special case
    file = Path.cwd()/'assets'/'json'/'melody.json'
    
    with file.open('r', encoding='utf-8') as melody:
        return json.load(melody)

def load_pogers():
    input = Path.cwd()/'assets'/'json'/'playlist_ids.json'
    output = Path.cwd()/'assets'/'json'/'playlists.json'
    bearer = get_bearer()
    load_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    print("Collecting playlists...")
    
    with input.open('r', encoding='utf-8') as i:
        ids = json.load(i)['playlists']
    
    combined = {
        "time": load_time,
        "playlists": []
    }
    
    with output.open('w', encoding='utf-8') as file:
        combined['playlists'].append(get_melody())
        print(f"Read melody is poger")
        for id in ids:
            playlist = get_playlist(id, bearer)
            name = playlist["name"]
            combined['playlists'].append(playlist)
            print(f"Read {name}")
        json.dump(combined, file, indent=4)
    
if __name__ == "__main__":
    load_pogers()