"""Command implementation
"""
from cleo import Command

from metrics import git


class GenerateCommand(Command):
    """
    Generate pyproject.toml from the source file

    generate
        {--r|repo= : git repository}
        {--d|dry-run : Only display the generated command.}
    """

    def handle(self):
        _repo = self.option("repo")
        print(_repo)
        git.iter_commits("https://github.com/calavia-org/online-ide")
