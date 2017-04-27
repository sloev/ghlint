import config
import repolint
from github import Github


def lint():
    ghlintr = config.read_ghlintrc()
    print ghlintr.sections()
    print ghlintr["RULES"]
    print ghlintr["RULES"]["editorconfig"]

    github = Github(config.GITHUB_USERNAME, config.GITHUB_PASSWORD)

    for repo in github.get_user().get_repos():
        repolint.repolint(repo)

if __name__ == "__main__":
    lint()
