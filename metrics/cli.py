#!/usr/bin/env python
"""entry point for metrics command
"""
from cleo import Application

from . import __version__
from .commands import GenerateCommand


application = Application("metrics", __version__, complete=True)
application.add(GenerateCommand())

if __name__ == "__main__":
    application.run()
