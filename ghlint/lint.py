from __future__ import print_function
from datetime import datetime
import config
from termcolor import cprint
from github.GithubException import UnknownObjectException


def lint(repo):
    # this is for debugging only
    #if repo.name != "TeamPilgrim":
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
            rule_protection(repo, ghlintrc)
            rule_old_pulls(repo, ghlintrc)

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
    rule = get_rule_value(repo, ghlintrc, "ghlintrc")
    if rule == "off":
        return

    condition = get_file_found(repo, ".ghlintrc")
    message = "File .ghlintrc not found"
    print_message(condition, rule, message)

def rule_editorconfig(repo, ghlintrc):
    rule = get_rule_value(repo, ghlintrc, "editorconfig")
    if rule == "off":
        return

    condition = get_file_found(repo, ".editorconfig")
    message = "File .editorconfig not found"
    print_message(condition, rule, message)

def rule_gitignore(repo, ghlintrc):
    rule = get_rule_value(repo, ghlintrc, "gitignore")
    if rule == "off":
        return

    condition = get_file_found(repo, ".gitignore")
    message = "File .gitignore not found"
    print_message(condition, rule, message)

def rule_protection(repo, ghlintrc):
    rule = get_rule_value(repo, ghlintrc, "protection")
    if rule == "off":
        return

    branch = repo.get_protected_branch(repo.default_branch)
    condition = branch.protected
    message = "Branch '" + repo.default_branch + "' not protected"
    print_message(condition, rule, message)

def rule_old_pulls(repo, ghlintrc):
    rule = get_rule_value(repo, ghlintrc, "rule_old_pulls")
    if rule == "off":
        return

    pulls = repo.get_pulls()
    for pull in pulls:
        pr_age = datetime.now() - pull.created_at
        pr_max_age = int(get_rule_value(repo, ghlintrc, "rule_old_pulls_max_age"))
        if pr_age.days >= pr_max_age and pull.state == "open":
            print("title: " + pull.title)
            print("url: " + pull.url)
            print("number: " + str(pull.number))
            print(pull.base)
            print(pull.head.label)
            print(pull.head.ref)
            print(repo.name + " " + pull.head.label[11:])

# - description
# - CONTRIBUTING.md
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
# license detection
# - https://developer.github.com/v3/licenses/#get-a-repositorys-license
# CI
# Node.js
# - npm
# - package.json
# Python
# - pypi
# master branch protection

