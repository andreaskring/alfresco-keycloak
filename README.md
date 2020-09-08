# Nice to know

[https://www.appsdeveloperblog.com/keycloak-rest-api-create-a-new-user/](https://www.appsdeveloperblog.com/keycloak-rest-api-create-a-new-user/)

# curl

Get token for admin-cli (enable acces type "confidential"):

```
$ curl -i -X POST -d 'grant_type=client_credentials' -d 'client_id=admin-cli' -d 'client_secret=...' "http://localhost:8180/auth/realms/alfresco/protocol/openid-connect/token"
```
