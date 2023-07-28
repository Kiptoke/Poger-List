from pathlib import Path
from utility import USER_TABLE, convertMS
import json

def get_playlists():
    file = Path.cwd()/'content'/'json'/'playlists.json'
    
    with file.open('r', encoding='utf-8') as playlists:
        return json.load(playlists)

# The two functions are helper functions to get user details and are not neccessary to update the site.
""" 
def get_users():
    playlists = get_playlists()["playlists"]
    reversed = dict((v, k) for k, v in USER_TABLE.items())
    
    for pl in playlists:
        name = pl["name"]
        users = set()
        for track in pl['tracks']['items']:
            id = track['added_by']['id']
            users.add(reversed[id])
            
        print(f"{name} - {users}")
    
def get_user_poges(user):
    playlists = get_playlists()["playlists"]
    participated = set()
    
    for pl in playlists:
        for track in pl['tracks']['items']:
            id = track['added_by']['id']
            if USER_TABLE[user] == id:
                participated.add(pl["name"])
            
    return participated 
    """

def get_user_songs(user, path):
    with path.open('r', encoding='utf-8') as playlist:
        data = json.load(playlist)
        songs = []
                
        for track in data['tracks']['items']:
            id = track['added_by']['id']
            if USER_TABLE[user] == id:
                song_name = track['track']['name']
                album = track['track']['album']
                length = convertMS(track['track']['duration_ms'])
                artists = []
                
                for artist in track['track']['artists']:
                    artists.append(artist['name'])
            
                song = {
                    'name': song_name,
                    'length': f"{length[0]}:{length[1]}",
                    'album': album['name'],
                    'artist': artists,
                }
                
                songs.append(song)
                
        return songs

def get_all_user_songs(user):
    playlists = get_playlists()["playlists"]
    full_list = []
    
    for pl in playlists:   
        path = Path.cwd()/'content'/'json'/'playlists'/f'{pl}.json'
        data = {
            'name': pl,
            'songs': get_user_songs(user, path)
        }
        if data['songs'] != []:
            full_list.append(data)
    
    output = {
        'user': user.title(),
        'id': USER_TABLE[user],
        'poges': full_list
    }
    
    return output

def user_publish():
    output = Path.cwd()/'content'/'json'/'users.json'
    users = []
    
    with output.open('w', encoding='utf-8') as file:
        for key in USER_TABLE:
           print(f"Processing user {key}")
           users.append(get_all_user_songs(key))
           
        j = {
            "users": users
        }
        
        json.dump(j, file, indent=4)

if __name__ == "__main__":
    user_publish()