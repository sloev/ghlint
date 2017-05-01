from datetime import datetime
import configparser
import os
from github import Github


GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")
GITHUB_PASSWORD = os.getenv("GITHUB_PASSWORD")


def main():
    ghlintrc = read_ghlintrc()
    github = Github(GITHUB_USERNAME, GITHUB_PASSWORD)

    repo_type = "owner"
    for repo in github.get_user().get_repos(repo_type):
        lint(repo, ghlintrc)

def lint(repo, ghlintr):
    print repo
    print ghlintr.sections()
    print ghlintr["RULES"]
    print ghlintr["RULES"]["editorconfig"]

    branches = repo.get_branches()
    for branch in branches:
        if branch.name == "master":
            has_editorconfig = False
            for file_in_root in repo.get_dir_contents("/"):
                if file_in_root.path == ".editorconfig":
                    has_editorconfig = True
                if file_in_root.path == ".gitignore":
                    has_gitignore = True
            if has_editorconfig != True:
                print "No .editorconfig"
            if has_gitignore != True:
                print "No .gitignore"

    pulls = repo.get_pulls()
    for pull in pulls:
        print "* " + pull.head.label[11:]
        pr_age = datetime.now() - pull.created_at
        if pr_age.days >= 7: # old pull requests
            print repo.name + " " + pull.head.label[11:]

def find_ghlintrc():
    ghlintrc = None

    if os.path.exists(".ghlintrc"):
        ghlintrc = os.path.abspath(".ghlintrc")

    return ghlintrc

def read_ghlintrc():
    config = configparser.ConfigParser()
    config.read(find_ghlintrc())

    return config


if __name__ == "__main__":
    main()
