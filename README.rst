ghlint
======

|build| |pypi|

Linting utility for GitHub.

Getting Started
---------------

Set the environment variables ``GITHUB_USERNAME`` and ``GITHUB_PASSWORD`` to your GitHub credentials. Alternatively, configure your username and `access token <https://github.com/settings/tokens>`_ in the ``[SETTINGS]`` section of the ``.ghlintrc`` file:

.. code-block::

    [SETTINGS]

    # GitHub username
    username=YOUR_USERNAME

    # GitHub password or personal access token
    password=YOUR_PASSWORD

Run
---

.. code-block:: sh

    pip install -r requirements.txt
    python ghlint/main.py

Next
----

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


.. |build| image:: https://img.shields.io/travis/martinbuberl/ghlint/master.svg?label=build
    :target: http://travis-ci.org/martinbuberl/ghlint

.. |pypi| image:: https://img.shields.io/pypi/v/ghlint.svg?label=pypi
    :target: https://pypi.python.org/pypi/ghlint
