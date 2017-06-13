from datetime import datetime
from termcolor import cprint
from ghlint import config

def lint(repo):
     # this is for debugging only
    if repo.name != "ghlint-foobar":
        return

    branches = repo.get_branches()
    for branch in branches:
        if branch.name == "master":
            file_ = repo.get_file_contents("/.ghlintrc")
            ghlintrc = config.merged(file_.decoded_content)

            print repo.name
            print ghlintrc.get("ALL", "editorconfig")


def foo(repo, ghlintrc):
    cprint(repo.name + " (", "white", end="")
    if repo.private is True:
        cprint("Private", "red", end="")
    else:
        cprint("Public", "green", end="")
    cprint(")", "white")

    print "this config"
    print ghlintrc.sections()

    branches = repo.get_branches()
    for branch in branches:
        if branch.name == "master":
            file_ = repo.get_file_contents("/.ghlintrc")
            decoded_content = "# Test " + "\r\n" + file_.decoded_content
            print decoded_content

            has_editorconfig = False
            has_gitignore = False

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
