import configparser
import os
import lint
from github import Github


def run(username, password):
    github = Github(username, password)
    ghlintrc = read_ghlintrc()

    repo_type = "owner"
    for repo in github.get_user().get_repos(repo_type):
        if repo.fork is False:
            if repo.name == "ghlint-foobar": # this is for debugging only
                lint.lint(repo, ghlintrc)

def find_ghlintrc():
    ghlintrc = None

    if os.path.exists(".ghlintrc"):
        ghlintrc = os.path.abspath(".ghlintrc")

    return ghlintrc

def read_ghlintrc():
    config = configparser.ConfigParser()
    config.read(find_ghlintrc())

    return config


def main():
    username = os.getenv("GITHUB_USERNAME")
    password = os.getenv("GITHUB_PASSWORD")

    run(username, password)

if __name__ == "__main__":
    main()
