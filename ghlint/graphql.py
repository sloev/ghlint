from __future__ import print_function
import requests
from requests.auth import HTTPBasicAuth
import config

def run(settings):
    username = settings["username"]
    password = settings["password"]

    response = requests.post("https://api.github.com/graphql",
                             auth=HTTPBasicAuth(username, password),
                             data="{ \"query\": \"query { viewer { login } }\" }")

    print(response.status_code)
    print(response.text)

def main():
    run(config.settings())

if __name__ == "__main__":
    main()
