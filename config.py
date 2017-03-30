"""Configuration settings"""
import os

GITHUB_USERNAME = os.getenv("GITHUB_USERNAME") or "YOUR_GITHUB_USERNAME"
GITHUB_PASSWORD = os.getenv("GITHUB_PASSWORD") or "YOUR_GITHUB_PASSWORD"

def find_ghlintrc():
    """search the ghlintrc file and return its path"""
    ghlintrc = None

    if os.path.exists('.ghlintrc'):
        ghlintrc = os.path.abspath('.ghlintrc')

    return ghlintrc

GHLINTRC = find_ghlintrc()
