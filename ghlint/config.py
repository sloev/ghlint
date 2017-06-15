try:
    import configparser
except ImportError:
    import ConfigParser as configparser
import os
from io import StringIO


GHLINTRC = ".ghlintrc"

def ghlintrc_path():
    path = None

    if os.path.exists(GHLINTRC):
        path = os.path.abspath(GHLINTRC)

    return path

def settings():
    items = dict(default().items("SETTINGS"))

    username = os.getenv("GITHUB_USERNAME") or items["username"]
    password = os.getenv("GITHUB_PASSWORD") or items["password"]
    account_type = items["account-type"] or "user"
    organization = items["organization"]
    repo_type = items["repo-type"] or "all"

    return {
        "username": username,
        "password": password,
        "account-type": account_type,
        "organization": organization,
        "repo-type": repo_type
    }

def default():
    parser = configparser.ConfigParser()
    parser.read(ghlintrc_path())

    return parser

def merged(ghlintrc_repo):
    buf = StringIO.StringIO(ghlintrc_repo)

    parser = default()
    parser.readfp(buf)

    return parser
