"""Repository linter"""
from datetime import datetime
from termcolor import cprint

def repolint(repo):
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
                if file_in_root.path == "LICENSE":
                    has_license = True
                if file_in_root.path == "README":
                    has_readme = True
            if has_editorconfig != True:
                cprint("No .editorconfig", "yellow")

    pulls = repo.get_pulls()
    for pr in pulls:
        print "* " + pr.head.label[11:]
        pr_age = datetime.now() - pr.created_at
        if pr_age.days >= 7: # old pull requests
            cprint(repo.name + " " + pr.head.label[11:], "yellow")

# # active branches
# - merged
# - un-merged
# # stale branches
# - merged
# - un-merged
# # open pull requests
# - proportion open:closed pull requests
# # open issues
# - proportion open:closed issues
# CI
# Node.js
# - npm
# - package.json
# Python
# - pypi
# master branch protection
