#
# import sys
# print(sys.version)
#
import config
import lint
from github import Github


def run(settings):
    github = Github(settings["username"], settings["password"])

    account_type = settings["account-type"]
    organization = settings["organization"]
    repo_type = settings["repo-type"]

    if account_type == "organization":
        repos = github.get_organization(organization).get_repos(repo_type)
    else:
        repos = github.get_user().get_repos(repo_type)

    # TODO, 8/15/2017: Implement API rate limit warning
    # print("{}".format(github.get_rate_limit().rate))

    for repo in repos:
        if repo.fork is False:
            lint.lint(repo)


def main():
    run(config.settings())

if __name__ == "__main__":
    main()
