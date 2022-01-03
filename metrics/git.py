"""Utility module for git operations
"""

from pydriller import Repository

def iter_commits():
    """Test function
    """
    for commit in Repository('https://github.com/calavia-org/online-ide').traverse_commits():
        print(commit.hash)
        print(commit.msg)
        print(commit.author.name)

        for file in commit.modified_files:
            print(file.filename, ' has changed')
