from urllib.parse import urlencode
import spotify_auth as sa 

client_id = '2476c1f2ab024aae8debc9146cd01926'
client_secret = '5628b40e45294570a9b115af35654b64'

spotify_client = sa.SpotifyAuth(client_id, client_secret)
spotify_client.perform_auth(show_auth=True)

access_token = spotify_client.access_token
print(access_token)

