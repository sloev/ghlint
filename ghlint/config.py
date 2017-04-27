import os


GITHUB_USERNAME = os.getenv("GITHUB_USERNAME") or "YOUR_GITHUB_USERNAME"
GITHUB_PASSWORD = os.getenv("GITHUB_PASSWORD") or "YOUR_GITHUB_PASSWORD"

def find_ghlintrc():
    ghlintrc = None

    if os.path.exists('.ghlintrc'):
        ghlintrc = os.path.abspath('.ghlintrc')

    return ghlintrc

GHLINTRC = find_ghlintrc()
