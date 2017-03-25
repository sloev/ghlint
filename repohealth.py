import ConfigParser
from github import Github

config = ConfigParser.RawConfigParser()
config.read("repohealth.cfg")

github = Github(config.get("GITHUB", "user"), config.get("GITHUB", "password"))

for repo in github.get_user().get_repos():
    print repo.name
