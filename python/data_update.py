import playlists
import users
import os

if __name__ == "__main__":
    playlists.load_playlists(os.getenv('client_id'), os.getenv('client_secret'))
    users.user_publish()