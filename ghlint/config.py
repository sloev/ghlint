import os
import configparser


GITHUB_USERNAME = os.getenv("GITHUB_USERNAME") or "YOUR_GITHUB_USERNAME"
GITHUB_PASSWORD = os.getenv("GITHUB_PASSWORD") or "YOUR_GITHUB_PASSWORD"

def find_ghlintrc():
    ghlintrc = None

    if os.path.exists(".ghlintrc"):
        ghlintrc = os.path.abspath(".ghlintrc")

    return ghlintrc

def read_ghlintrc():
    config = configparser.ConfigParser()
    config.read(find_ghlintrc())

    return config
