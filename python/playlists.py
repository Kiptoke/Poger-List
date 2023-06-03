from pathlib import Path
import datetime
import json
import requests
import os
    
def get_bearer(id, secret):
    params = {
        'grant_type': "client_credentials",
        'client_id': id,
        'client_secret': secret
    }
    print(params)
    headers = {
        'Content-Type': "application/x-www-form-urlencoded"
    }
    bearer = requests.post(
        "https://accounts.spotify.com/api/token",
        params = params,
        headers = headers
    ).json()
    print(bearer)
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
    
    image = Path.cwd()/'content'/'pogers'
    img = requests.get(pl['images'][0]['url']).content
    with open(f"{image}/{pl['name']}.jpg", 'wb') as handler:
        handler.write(img)
    
    return pl

def get_melody():
    # "65rLedogOjLqWp938fZCNu", melody is poger - requires special case
    file = Path.cwd()/'content'/'json'/'melody.json'
    image = Path.cwd()/'content'/'pogers'
    
    with file.open('r', encoding='utf-8') as melody:
        md = json.load(melody)
        img = requests.get(md['images'][0]['url']).content
        with open(f"{image}/{md['name']}.jpg", 'wb') as handler:
            handler.write(img)
        return md

def load_playlists(client_id, client_secret):
    input = Path.cwd()/'content'/'json'/'playlist_ids.json'
    output = Path.cwd()/'content'/'json'/'playlists.json'
    bearer = get_bearer(client_id, client_secret)
    load_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    print("Collecting playlists...")
    
    with input.open('r', encoding='utf-8') as i:
        ids = json.load(i)['playlists']
    
    combined = {
        "time": load_time,
        "playlists": []
    }
    
    combined['playlists'].append(get_melody())
    print(f"Read melody is poger")
        
    for id in ids:
        playlist = get_playlist(id, bearer)
        name = playlist["name"]
        combined['playlists'].append(playlist)
        print(f"Read {name}")
            
    with output.open('w', encoding='utf-8') as file:
        json.dump(combined, file, indent=4)     
    
if __name__ == "__main__":
    load_playlists()