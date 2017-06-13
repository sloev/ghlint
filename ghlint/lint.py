from datetime import datetime
from termcolor import cprint
from ghlint import config

def lint(repo):
     # this is for debugging only
    if repo.name != "ghlint-foobar":
        return

    branches = repo.get_branches()
    for branch in branches:
        if branch.name == repo.default_branch:
            file_ = repo.get_file_contents("/.ghlintrc")
            ghlintrc = config.merged(file_.decoded_content)

            if repo.private:
                print repo.full_name + " [Private]"
            else:
                print repo.full_name

            rule_editorconfig(repo, ghlintrc)
            rule_gitignore(repo, ghlintrc)


def rule_editorconfig(repo, ghlintrc):
    print root_has_file(repo, ".editorconfig")
    print ghlintrc.get("ALL", "editorconfig")

def rule_gitignore(repo, ghlintrc):
    print root_has_file(repo, ".gitignore")
    print ghlintrc.get("ALL", "gitignore")

def root_has_file(repo, filename):
    for file_in_root in repo.get_dir_contents("/"):
        if file_in_root == filename:
            return True

    return False

def foo(repo, ghlintrc):
    pulls = repo.get_pulls()
    for pull in pulls:
        print "* " + pull.head.label[11:]
        pr_age = datetime.now() - pull.created_at
        if pr_age.days >= 7: # old pull requests
            print repo.name + " " + pull.head.label[11:]
