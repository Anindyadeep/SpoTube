import json
import requests
import base64
import datetime

client_id = '2476c1f2ab024aae8debc9146cd01926'
client_secret = '5628b40e45294570a9b115af35654b64'

token_url = 'https://accounts.spotify.com/api/token'
token_method = 'POST'

client_creds = f'{client_id}:{client_secret}'
client_creds_base64 = base64.b64encode(client_creds.encode())

token_data = {
    'grant_type': 'client_credentials'
}

token_headers = {
    'Authorization': f'Basic {client_creds_base64.decode()}'
}

r = requests.post(
                url = token_url,
                data = token_data,
                headers = token_headers)

if r.status_code in range(200, 299):
    token_response_data = r.json()
    now = datetime.datetime.now()

    access_token = token_response_data['access_token']
    expires_in = token_response_data['expires_in'] # in seconds
    expires = now + datetime.timedelta(seconds=expires_in)

    did_expire = expires < now
    print(json.dumps(token_response_data))
