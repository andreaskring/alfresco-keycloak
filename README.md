# Nice to know

[https://www.appsdeveloperblog.com/keycloak-rest-api-create-a-new-user/](https://www.appsdeveloperblog.com/keycloak-rest-api-create-a-new-user/)

# curl

Get token for admin-cli (enable acces type "confidential"):

```
$ curl -i -X POST -d 'grant_type=client_credentials' -d 'client_id=admin-cli' -d 'client_secret=...' "http://localhost:8180/auth/realms/alfresco/protocol/openid-connect/token"
```

# Allow admin-cli to enable/disable other client in realm

See Python script in the utils folder.

## Settings for admin-cli

1. Access Type: confidential
1. (Direct Access Grants Enabled: off)
1. Service Accounts Enabled: on
1. Service Account Roles -> Client Roles -> realm-management -> add manage-clients
