#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# Copyright (c) Merchise Autrement [~º/~] and Contributors
# All rights reserved.
#
# This is free software; you can do what the LICENCE file allows you to.
#

from __future__ import (division as _py3_division,
                        print_function as _py3_print,
                        absolute_import as _py3_abs_imports)


def test_ppformat_rtype():
    from xoutil.future.pprint import ppformat
    from xoutil.eight import text_type
    o = [list(range(i+1)) for i in range(10)]
    assert type(ppformat(o)) is text_type
