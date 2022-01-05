"""Utility module for git operations
"""

from pydriller import Repository


def iter_commits(repository_url: str) -> None:
    """Test function"""
    for commit in Repository(repository_url).traverse_commits():
        print(commit.hash)
