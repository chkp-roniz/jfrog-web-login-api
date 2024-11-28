# Web Login to the JFrog Platform
Integrate the 'jf login' web login command behavior to your service or CLI using JFrog undocumented Access APIs.
The web login command allows you to login to the JFrog platform through a web browser, making the process interactive and user-friendly.

## Access REST APIs
### Base URL
The Platform REST URL is constructed of:
```
<JFrog URL>/<Service Context>/

For example:

# Using your JFrog URL 
http://artifactory.mycompany.com/access/
```
### Request Web Client Access

**Usage**: `POST api/v2/authentication/jfrog_client_login/request -H "Content-Type: application/json"`

**Consumes**: `application/json`

```
POST /api/v2/authentication/jfrog_client_login/request
{
 "session": "274f11d9-9d2f-4fd3-813d-a6551c8dd916",    // generated uuid
}
```
### Get Web Client Access Token

**Usage**: `GET api/v2/authentication/jfrog_client_login/token/{uuid}`

**Sample Output:**
```
{
  "token_id" : "3693ad1a-fdb7-4ca4-b0d2-bed0b08b7717",
  "access_token" : "****",
  "refresh_token" : "ba66b7ec-c106-4b73-84b2-dba34bf4d96f",
  "expires_in" : 31536000,
  "scope" : "****",
  "token_type" : "Bearer",
  "username" : "username@mycompany.com"
}
```
![image](https://github.com/user-attachments/assets/755c5fc2-f05b-4c0f-95f7-a265059d0fc6)
![image](https://github.com/user-attachments/assets/16398ca1-89a6-4ff1-b7cf-6ecaa710a4a6)
