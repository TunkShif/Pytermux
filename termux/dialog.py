#!/usr/bin/env python
# -*- coding:utf-8 -*-
from termux import _run

cmd = "termux-dialog"


def confirm(hint="Hint", title="Title"):
    data = _run(f"{cmd} -i {hint} -t {title}", is_json=True)
    return data
