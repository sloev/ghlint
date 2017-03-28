"""Repository linter"""
from datetime import datetime
from termcolor import cprint

def repolint(repo):
    print repo.name

    branches = repo.get_branches()
    for branch in branches:
        if branch.name == "master":
            for file in repo.get_dir_contents("/"):
                print file
                # check for
                # - README
                # - LICENSE
                # - .gitignore
                # - .editorconfig

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
