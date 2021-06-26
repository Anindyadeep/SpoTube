import json
import requests
import  datetime
import base64

class SpotifyAuth:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.token_url = 'https://accounts.spotify.com/api/token'
        self.token_method = 'POST'

        self.access_token = None
        self.token_expires = datetime.datetime.now()
        self.access_token_did_expire = True 
    

    def get_token_data(self):
        token_data = {
            'grant_type': 'client_credentials'
        }
        return token_data

    def get_client_credentials(self, decode = False):
        if self.client_secret == None or self.client_secret == None:
            raise Exception("You must include your client id and its secret keys")

        client_creds = f'{self.client_id}:{self.client_secret}'
        client_creds_base64 = base64.b64encode(client_creds.encode())

        if decode:
            client_creds_base64_decode = client_creds_base64.decode()
            return client_creds_base64_decode
        
        else:
            return client_creds_base64
    
    def get_token_header(self):
        client_credentials = self.get_client_credentials(decode=True)
        token_headers = {
            'Authorization': f'Basic {client_credentials}'
        }
        return token_headers
        
    
    def perform_auth(self, show_auth = False):
        user_token_data = self.get_token_data()
        user_token_headers = self.get_token_header()

        r = requests.post(url=self.token_url, data=user_token_data, headers=user_token_headers)
        if r.status_code in range(200, 299):
            if show_auth:
                print(json.dumps(r.json()))
            
            token_response_data = r.json()
            now = datetime.datetime.now()

            self.access_token = token_response_data['access_token']
            access_token_expires_in = token_response_data['expires_in']
            self.token_expires = now + datetime.timedelta(seconds=access_token_expires_in)
            self.access_token_did_expire = self.token_expires < now 

            return True 
        return False 


if __name__ == '__main__':
    client_id = '2476c1f2ab024aae8debc9146cd01926'
    client_secret = '5628b40e45294570a9b115af35654b64'
    spAPI = SpotifyAuth(client_id, client_secret)

    print(spAPI.perform_auth(show_auth=True))
    print(spAPI.access_token)

