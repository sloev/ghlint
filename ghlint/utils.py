import configparser
import os
import StringIO


def get_config():
    username = os.getenv("GITHUB_USERNAME")
    password = os.getenv("GITHUB_PASSWORD")
    ghlintrc = ghlintrc_default()
    account_type = ghlintrc.get("CONFIG", "account-type") or "user"
    organization = ghlintrc.get("CONFIG", "organization")
    repo_type = ghlintrc.get("CONFIG", "repo-type") or "all"

    config = {
        "username": username,
        "password": password,
        "account-type": account_type,
        "organization": organization,
        "repo-type": repo_type
    }

    return config

def ghlintrc_path():
    path = None

    if os.path.exists(".ghlintrc"):
        path = os.path.abspath(".ghlintrc")

    return path

def ghlintrc_default():
    parser = configparser.ConfigParser()
    parser.read(ghlintrc_path())

    return parser

def ghlintrc_merged(ghlintrc_repo):
    buf = StringIO.StringIO(ghlintrc_repo)

    parser = ghlintrc_default()
    parser.readfp(buf)

    return parser
