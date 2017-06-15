from __future__ import print_function
from datetime import datetime
from termcolor import cprint
import config
from github.GithubException import UnknownObjectException

def lint(repo):
    # this is for debugging only
    #if repo.name != "boilerplate-api":
    #    return

    branches = repo.get_branches()
    for branch in branches:
        if branch.name == repo.default_branch:
            try:
                file_ = repo.get_file_contents("/.ghlintrc")
                ghlintrc = config.merged(file_.decoded_content)
            except UnknownObjectException:
                ghlintrc = config.default()

            if repo.private:
                print(repo.full_name + " [Private]")
            else:
                print(repo.full_name)

            rule_ghlintrc(repo, ghlintrc)
            rule_editorconfig(repo, ghlintrc)
            rule_gitignore(repo, ghlintrc)

def get_file_found(repo, file_name):
    root = "/"

    for file_root in repo.get_dir_contents(root):
        if file_root.path == file_name:
            return True

    return False

def get_rule_value(repo, ghlintrc, rule_name):
    value = ghlintrc.get("ALL", rule_name)

    if repo.private:
        if ghlintrc.has_option("PRIVATE", rule_name):
            value = ghlintrc.get("PRIVATE", rule_name)

    return value

def print_message(condition, rule, message):
    if not condition:
        if rule == "warn":
            cprint(message, "yellow")
        elif rule == "error":
            cprint(message, "red")

def rule_ghlintrc(repo, ghlintrc):
    condition = get_file_found(repo, ".ghlintrc")
    rule = get_rule_value(repo, ghlintrc, "ghlintrc")
    message = "File .ghlintrc not found"
    print_message(condition, rule, message)

def rule_editorconfig(repo, ghlintrc):
    condition = get_file_found(repo, ".editorconfig")
    rule = get_rule_value(repo, ghlintrc, "editorconfig")
    message = "File .editorconfig not found"
    print_message(condition, rule, message)

def rule_gitignore(repo, ghlintrc):
    condition = get_file_found(repo, ".gitignore")
    rule = get_rule_value(repo, ghlintrc, "gitignore")
    message = "File .gitignore not found"
    print_message(condition, rule, message)

#def foo(repo, ghlintrc):
#    pulls = repo.get_pulls()
#    for pull in pulls:
#        print("* " + pull.head.label[11:])
#        pr_age = datetime.now() - pull.created_at
#        if pr_age.days >= 7: # old pull requests
#            print(repo.name + " " + pull.head.label[11:])
