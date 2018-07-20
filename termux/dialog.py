#!/usr/bin/env python
# -*- coding:utf-8 -*-
from termux import _run

_cmd = "termux-dialog"


def confirm(hint="Hint", title="Title"):
    """Confirm Dialog
    Returns:
        dict
    """
    data = _run(f"{_cmd} -i {hint} -t {title}", is_json=True)
    return data


def checkbox(values: list, title="Title"):
    """Checkbox Dialog
    Args:
        values: a string list
    Returns:
        dict
    """
    v = ", ".join(values)
    data = _run(f"{_cmd} -v {v} -t {title}", is_json=True)
    return data


def counter():
    pass
