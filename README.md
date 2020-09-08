# Nice to know

[https://www.appsdeveloperblog.com/keycloak-rest-api-create-a-new-user/](https://www.appsdeveloperblog.com/keycloak-rest-api-create-a-new-user/)

# curl

Get token for admin-cli (enable acces type "confidential"):

```
$ curl -i -X POST -d 'grant_type=client_credentials' -d 'client_id=admin-cli' -d 'client_secret=...' "http://localhost:8180/auth/realms/alfresco/protocol/openid-connect/token"
```

# About clients, roles, scopes...

## Settings for admin-cli

1. Access Type: confidential
1. Service Accounts Enabled: on
1. Service Account Roles -> Client Roles -> realm-management -> assign all roles (it is in fact the manage-client one that is important)

## Settings for realm-management client

These settings are not necessary:

1. Access Type: bearer-only
1. Roles -> manage-clients -> Composite Roles: on -> Client Roles: realm-management -> add all


## Users

This setting is not really important when using client credentials. 
An admin user has been set with the client roles for `realm-management` to "all roles assigned"

