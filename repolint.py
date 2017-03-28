"""Repository linter"""
from datetime import datetime
from termcolor import cprint

def repolint(repo):
    print repo.name

    branches = repo.get_branches()
    for branch in branches:
        print "+ " + branch.name

    pulls = repo.get_pulls()
    for pr in pulls:
        print "* " + pr.head.label[11:]
        pr_age = datetime.now() - pr.created_at
        if pr_age.days >= 7: # old pull requests
            cprint(repo.name + " " + pr.head.label[11:], "yellow")
