"""Basic console implementation"""
import config
from github import Github

GITHUB = Github(config.GITHUB_USERNAME, config.GITHUB_PASSWORD)

for repo in GITHUB.get_user().get_repos():
    print repo.name
