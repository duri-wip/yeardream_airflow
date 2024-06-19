import requests
# client_id, authorize_code 노출 주의, 실제 값은 임시로만 넣고 Git에 올라가지 않도록 유의

client_id = 'facaadac563a8dc6439b19b86500221b'
redirect_uri = 'https://example.com/oauth'
authorize_code = 'Y6jvbIe59GeYlic-JoQBkLBfcA1ztXaiCGhkl0SjjXPIhWs2T4XJzAAAAAQKPXPsAAABkC3zEGm2W8wW6V7rJg'


token_url = 'https://kauth.kakao.com/oauth/token'
data = {
    'grant_type': 'authorization_code',
    'client_id': client_id,
    'redirect_uri': redirect_uri,
    'code': authorize_code,
    }

response = requests.post(token_url, data=data)
tokens = response.json()
print(tokens)