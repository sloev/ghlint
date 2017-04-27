import config
import repolint
from github import Github

def lint():
    GITHUB = Github(config.GITHUB_USERNAME, config.GITHUB_PASSWORD)

    for repo in GITHUB.get_user().get_repos():
        repolint.repolint(repo)

if __name__ == "__main__":
    lint()
