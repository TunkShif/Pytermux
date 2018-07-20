#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os as _os
import json as _json

__version__ = "0.1"


def _run(commands, is_json=False):
    """Run Commands

    Run a shell command and return output

    Args:
        commands: shell command
        is_json: whether the output is json string
    Returns:
        the output or a dict
    """
    cmd = _os.popen(commands)
    if is_json:
        return _json.loads(cmd.read())
    else:
        return cmd.read()
