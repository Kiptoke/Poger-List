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
    
    image = Path.cwd()/'content'/'pogers'
    img = requests.get(pl['images'][0]['url']).content
    if pl['name'] == "pogern't":
        with open(f"{image}/pogernt.jpg", 'wb') as handler:
            handler.write(img)
    else:
        with open(f"{image}/{pl['name']}.jpg", 'wb') as handler:
            handler.write(img)
    
    return pl

def get_melody():
    # "65rLedogOjLqWp938fZCNu", melody is poger - requires special case
    file = Path.cwd()/'content'/'json'/'playalists'/'melody is poger.json'
    image = Path.cwd()/'content'/'pogers'
    
    with file.open('r', encoding='utf-8') as melody:
        md = json.load(melody)
        img = requests.get(md['images'][0]['url']).content
        with open(f"{image}/{md['name']}.jpg", 'wb') as handler:
            handler.write(img)
        return md

def load_playlists(client_id, client_secret):
    input = Path.cwd()/'content'/'json'/'playlist_ids.json'
    pl_output = Path.cwd()/'content'/'json'/'playlists.json'
    bearer = get_bearer(client_id, client_secret)
    load_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    pl = {"playlists": []}
    
    print("Collecting playlists...")
    
    with input.open('r', encoding='utf-8') as i:
        ids = json.load(i)['playlists']
    
    print(f"Read melody is poger")  # Melody is Poger is manually made, so this is printed for consistency
    pl['playlists'].append("melody is poger")
        
    for id in ids:
        playlist = get_playlist(id, bearer)
        name = playlist["name"]
        playlist['time'] = load_time
        print(f"Read {name}")
        
        if name == "pogern't":
            name = "pogernt"
        
        pl['playlists'].append(name)
        output = Path.cwd()/'content'/'json'/'playlists'/f"{name}.json"
            
        with output.open('w', encoding='utf-8') as file:
            json.dump(playlist, file, indent=4)     
    
    with pl_output.open('w', encoding='utf-8') as file:
            json.dump(pl, file, indent=4)     

# This purely was made to test what the length of all poges was   
def question(client_id, client_secret):
    input = Path.cwd()/'content'/'json'/'playlist_ids.json'
    pl_output = Path.cwd()/'content'/'json'/'playlists.json'
    bearer = get_bearer(client_id, client_secret)
    load_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    pl = {"playlists": []}
    
    print("Collecting playlists...")
    
    with input.open('r', encoding='utf-8') as i:
        ids = json.load(i)['playlists']
    
    print(f"Read melody is poger")  # Melody is Poger is manually made, so this is printed for consistency
    pl['playlists'].append("melody is poger")
        
    for id in ids:
        playlist = get_playlist(id, bearer)
        name = playlist["name"]
        playlist['time'] = load_time
        print(f"Read {name}")
        
        if name == "pogern't":
            name = "pogernt"
        
        pl['playlists'].append(name)
        
    print(pl)   
            
if __name__ == "__main__":
    load_playlists()