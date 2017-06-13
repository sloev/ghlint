import os
import lint
import utils
from github import Github


def run(config):
    github = Github(config["username"], config["password"])

    account_type = config["account-type"]
    organization = config["organization"]
    repo_type = config["repo-type"]

    if account_type == "organization":
        repos = github.get_organization(organization).get_repos(repo_type)
    else:
        repos = github.get_user().get_repos(repo_type)

    for repo in repos:
        if repo.fork is False:
            lint.lint(repo)


def main():
    run(utils.get_config())

if __name__ == "__main__":
    main()
