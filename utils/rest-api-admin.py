import json
import requests

REALM = 'alfresco'
CLIENT_SECRET = '48cfa07e-adff-4a63-a17c-493f84546f2b'

# NOT the same as client-id (Keycloak thing...)
# E.g.
# client-id = alfresco
# "id of client" = e315ead7-c626-4b4e-9eff-21d0d529b1bc
CUSTOM_ID_CLIENT = '6a3422ce-92e7-4d71-a705-116dc3e85bf3'


token_url = f'http://localhost:8280/auth/realms/{REALM}' \
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

# Get list of clients

CLIENTS_URL = f'http://localhost:8280/auth/admin/realms/{REALM}/clients'
r = requests.get(CLIENTS_URL, headers=headers)
print(r.status_code, r.url)
print(json.dumps(r.json(), indent=2))

# Disable client

payload = {
    'enabled': False
}

CUSTOM_CLIENT_URL = f'http://localhost:8280/auth/admin/realms/{REALM}' \
                    f'/clients/{CUSTOM_ID_CLIENT}'
r = requests.put(CUSTOM_CLIENT_URL, json=payload, headers=headers)
print(r.status_code, r.url)
