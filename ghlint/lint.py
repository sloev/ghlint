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
                print("{} [Private]".format(repo.full_name))
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
    message = "Branch '{}' not protected".format(repo.default_branch)
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
            message = "Pull request #{} '{}' is {} days old".format(pull.number, pull.title, pull_age.days)
            print_message(rule, message)

def rule_loose_branch(repo, ghlintrc):
    rule = get_rule_value(repo, ghlintrc, "loose-branch")
    if rule == "off":
        return

    branches = repo.get_branches()
    branch_names = []
    for branch in branches:
        branch_names.append(branch.name)

    pulls = repo.get_pulls()
    pull_refs = []
    for pull in pulls:
        pull_refs.append(pull.head.ref)

    loose_branch_names = list(set(branch_names).difference(pull_refs))
    for loose_branch_name in loose_branch_names:
        if loose_branch_name != repo.default_branch:
            message = "Branch '{}' without pull request".format(loose_branch_name)
            print_message(rule, message)
