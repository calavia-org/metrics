#!/usr/bin/env python
"""entry point for metrics command
"""
from cleo import Application

from .commands import GenerateCommand

application = Application("metrics", "0.1.0", complete=True)
application.add(GenerateCommand())
