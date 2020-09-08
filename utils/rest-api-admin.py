import requests

REALM = 'hurra'
CLIENT_SECRET = '1db29fac-072b-4151-a916-2955780bf2ed'

# NOT the same as client-id (Keycloak thing...)
# E.g.
# client-id = alfresco
# "id of client" = e315ead7-c626-4b4e-9eff-21d0d529b1bc
CUSTOM_ID_CLIENT = 'e315ead7-c626-4b4e-9eff-21d0d529b1bc'


token_url = f'http://localhost:8180/auth/realms/{REALM}' \
            f'/protocol/openid-connect/token'

# Get token

payload = {
    'client_id': 'admin-cli',
    'client_secret': CLIENT_SECRET,
    'grant_type': 'client_credentials'
}

r = requests.post(token_url, data=payload)
print(r.status_code, r.url)
token = r.json()['access_token']

headers = {
    'Authorization': f'bearer {token}'
}

# Disable client

payload = {
    'enabled': False
}

CLIENT_URL = f'http://localhost:8180/auth/admin/realms/{REALM}' \
             f'/clients/{CUSTOM_ID_CLIENT}'
r = requests.put(CLIENT_URL, json=payload, headers=headers)
print(r.status_code, r.url)
