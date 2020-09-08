import requests


TOKEN_URL = 'http://localhost:8180/auth/realms/alfresco/protocol/openid-connect/token'

# Get token

payload = {
    'client_id': 'admin-cli',
#    'username': 'admin',
#    'password': 'admin',
    'client_secret': 'b85e1c8b-4349-4605-8a3c-58781711f673',
#    'client_secret': '7086a0bb-9767-45db-ab2b-53556a37cfc8',
#    'client_secret': '8eb882c8-c349-4e4c-8bda-1c02f8313486',
    'grant_type': 'client_credentials'
#    'grant_type': 'password'
}

r = requests.post(TOKEN_URL, data=payload)
print(r.status_code, r.url)
token = r.json()['access_token']

headers = {
    'Authorization': f'bearer {token}'
}

# Create user

payload = {
    "firstName": "Bruce",
    "lastName": "Lee",
    "email": "test@test.com",
    "enabled": True,
    "username": "bruce"
}

USER_URL = 'http://localhost:8180/auth/admin/realms/alfresco/users'
# r = requests.post(USER_URL, json=payload, headers=headers)
# print(r.status_code)

# Disable client

payload = {
    'id': '8eb882c8-c349-4e4c-8bda-1c02f8313486',
#    'clientId': 'alfresco',
    'enabled': False
}

CLIENT_URL = 'http://localhost:8180/auth/admin/realms/alfresco/clients/814dac5b-c726-4e4a-90eb-0d393492a7f3'
#CLIENT_URL = 'http://localhost:8180/auth/admin/realms/alfresco/clients/65b36272-912d-4c9b-9ba3-6cd6dd69703e'
r = requests.put(CLIENT_URL, json=payload, headers=headers)
print(r.status_code, r.url)
