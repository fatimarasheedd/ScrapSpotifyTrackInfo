from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json
from PIL import Image

load_dotenv()

# make sure to set these environment variables in the .env folder
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

# getting the spotify access token using the client id and client secret
def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode('utf-8')
    auth_base64 = str(base64.b64encode(auth_bytes), 'utf-8')

    url = 'https://accounts.spotify.com/api/token'
    headers = {
        'Authorization': 'Basic ' + auth_base64,
        'Content-type': 'application/x-www-form-urlencoded'
    }
    data = {'grant_type': 'client_credentials'}
    result = post(url, headers=headers, data=data)
    # convert data to python dictionary
    json_result = json.loads(result.content)
    token = json_result['access_token']
    return token

def get_auth_header(token):
    return {'Authorization': 'Bearer ' + token}

# get the song id based off library 
def get_song_id(token, song_name, artist):
    url = 'https://api.spotify.com/v1/search'
    headers = get_auth_header(token)
    query = f"?q=track:'{song_name}' artist:'{artist}'&type=track&limit=1"
    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)['tracks']['items']
    if len(json_result) == 0:
        print("No results found")
        return None
    
    return json_result[0]['id']

# get the song features based off song id
def get_song_features(token, song_id):
    url = f'https://api.spotify.com/v1/audio-features/{song_id}'
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)
    energy = json_result['energy']
    valence = json_result['valence']
    return energy, valence

# get album cover based off song id
def get_album_cover(token, song_id, song_name, artist):
    url = f'https://api.spotify.com/v1/tracks/{song_id}'
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)
    album_cover_url = json_result['album']['images'][0]['url']

    response = get(album_cover_url, stream=True)
    response.raise_for_status()

    file_name = f"{song_name}-{artist}.jpg"

    with open(file_name, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)

    return Image.open(file_name)


token = get_token()

