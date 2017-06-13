ghlint
======

Linting utility for GitHub.

Getting Started
---------------

Set the environment variables `GITHUB_USERNAME` and `GITHUB_PASSWORD` to your GitHub credentials. Alternatively, configure your username and `access token <https://github.com/settings/tokens>`_ in the settings ``[SETTINGS]`` of the ``.ghlintrc`` file:

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
