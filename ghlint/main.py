import config
from datetime import datetime
from github import Github


def main():
    ghlintr = config.read_ghlintrc()
    print ghlintr.sections()
    print ghlintr["RULES"]
    print ghlintr["RULES"]["editorconfig"]

    github = Github(config.GITHUB_USERNAME, config.GITHUB_PASSWORD)

    for repo in github.get_user().get_repos():
        lint(repo)

def lint(repo):
    print repo.name

    branches = repo.get_branches()
    for branch in branches:
        if branch.name == "master":
            has_editorconfig = False
            for file_in_root in repo.get_dir_contents("/"):
                if file_in_root.path == ".editorconfig":
                    has_editorconfig = True
                if file_in_root.path == ".gitignore":
                    has_gitignore = True
                if file_in_root.path == "LICENSE": # LICENSE.txt (or LICENSE.md
                    has_license = True
                if file_in_root.path == "README":
                    has_readme = True
            if has_editorconfig != True:
                print "No .editorconfig"

    pulls = repo.get_pulls()
    for pull in pulls:
        print "* " + pull.head.label[11:]
        pr_age = datetime.now() - pull.created_at
        if pr_age.days >= 7: # old pull requests
            print repo.name + " " + pull.head.label[11:]


if __name__ == "__main__":
    main()
