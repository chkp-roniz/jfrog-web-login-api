import requests
import json
import uuid
import webbrowser
import time

JF_URL = "https://artifactory.mycompany.com"
JF_ACCESS_SERVICE = "access"
JF_BASE_CLIENT_LOGIN_API = "api/v2/authentication/jfrog_client_login"
JF_REQUEST_API = "request"
JF_TOKEN_API = "token"
JF_CLIENT_LOGIN_API = f"{JF_URL}/{JF_ACCESS_SERVICE}/{JF_BASE_CLIENT_LOGIN_API}"

def get_token():
    """
    Generates a unique session token, prompts the user to log in via a web browser,
    and retrieves an access token from the server.
    The function performs the following steps:
    1. Generates a unique UUID string.
    2. Sends a POST request to initiate a session with the generated UUID.
    3. Prompts the user to log in via their web browser using the generated UUID.
    4. Attempts to open the login URL in the default web browser.
    5. Polls the server for an access token up to 5 times, waiting 5 seconds between each attempt.
    6. Returns the access token if successful, otherwise returns None.
    Returns:
        str: The access token if the login is successful, otherwise None.
    """
    uuid_str = str(uuid.uuid4())
    requests.post(
        f"{JF_CLIENT_LOGIN_API}/{JF_REQUEST_API}",
        data=json.dumps({"session": uuid_str}),
        headers={"Content-Type": "application/json"},
    )
    input(
        f"After logging in via your web browser, please enter the code if prompted: \033[1m{uuid_str[-4:]}\033[0m..."
    )
    if webbrowser.open(
        f"{JF_URL}/ui/login?jfClientSession={uuid_str}&jfClientName=JFrog-CLI&jfClientCode=1"
    ):

        for _ in range(5):
            response = requests.get(f"{JF_CLIENT_LOGIN_API}/{JF_TOKEN_API}/{uuid_str}")
            if response.status_code == 200:
                return response.json().get("access_token", None)

            time.sleep(5)

    return None
