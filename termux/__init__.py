#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import json

__version__ = "0.1"


def _run(commands, is_json=False):
    """Run a shell command and return output

    Args:
        commands: shell command
        is_json: whether the output is json string

    Returns:
        the output or a dict
    """
    cmd = os.popen(commands)
    if json:
        return json.loads(cmd.read())
    else:
        return cmd.read()
