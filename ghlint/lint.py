from __future__ import print_function
from datetime import datetime
import config
from termcolor import cprint
from github.GithubException import UnknownObjectException


def lint(repo):
    # this is for debugging only
    if repo.name != "ghlint-foobar":
        return

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

            rule_gitignore(repo, ghlintrc)
            rule_contributing(repo, ghlintrc)
            rule_editorconfig(repo, ghlintrc)
            rule_ghlintrc(repo, ghlintrc)
            rule_protection(repo, ghlintrc)
            rule_old_pull(repo, ghlintrc)
            rule_loose_branch(repo, ghlintrc)

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

def print_message(rule, message):
    if rule == "warn":
        cprint(message, "yellow")
    elif rule == "error":
        cprint(message, "red")

def rule_gitignore(repo, ghlintrc):
    rule = get_rule_value(repo, ghlintrc, "gitignore")
    if rule == "off":
        return

    message = "File .gitignore not found"
    if not get_file_found(repo, ".gitignore"):
        print_message(rule, message)

def rule_contributing(repo, ghlintrc):
    rule = get_rule_value(repo, ghlintrc, "contributing")
    if rule == "off":
        return

    message = "File CONTRIBUTING not found"
    if not get_file_found(repo, "CONTRIBUTING"):
        print_message(rule, message)

def rule_editorconfig(repo, ghlintrc):
    rule = get_rule_value(repo, ghlintrc, "editorconfig")
    if rule == "off":
        return

    message = "File .editorconfig not found"
    if not get_file_found(repo, ".editorconfig"):
        print_message(rule, message)

def rule_ghlintrc(repo, ghlintrc):
    rule = get_rule_value(repo, ghlintrc, "ghlintrc")
    if rule == "off":
        return

    message = "File .ghlintrc not found"
    if not get_file_found(repo, ".ghlintrc"):
        print_message(rule, message)

def rule_protection(repo, ghlintrc):
    rule = get_rule_value(repo, ghlintrc, "protection")
    if rule == "off":
        return

    branch = repo.get_protected_branch(repo.default_branch)
    message = "Branch '" + repo.default_branch + "' not protected"
    if not branch.protected:
        print_message(rule, message)

def rule_old_pull(repo, ghlintrc):
    rule = get_rule_value(repo, ghlintrc, "old-pull")
    if rule == "off":
        return

    pulls = repo.get_pulls()
    for pull in pulls:
        pull_age = datetime.now() - pull.created_at
        pull_max_age = int(get_rule_value(repo, ghlintrc, "old-pull-max-age"))
        if pull_age.days >= pull_max_age and pull.state == "open":
            message = "Pull request #" + str(pull.number) + " '" + pull.title + "' is " + str(pull_age.days) + " days old"
            print_message(rule, message)

def rule_loose_branch(repo, ghlintrc):
    branches = repo.get_branches()
    for branch in branches:
        print("x: {}".format(branch.name))
