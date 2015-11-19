#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# ---------------------------------------------------------------------
# xoutil.keywords
# ---------------------------------------------------------------------
# Copyright (c) 2015 Merchise Autrement and Contributors
# All rights reserved.
#
# This is free software; you can redistribute it and/or modify it under the
# terms of the LICENCE attached (see LICENCE file) in the distribution
# package.
#
# Created on 2015-11-17

'''Tools for manage Python keywords as names.

Reserved Python keywords can't be used as attribute names, so this module
functions use the convention of rename the name using an underscore as
suffix when a reserved keyword is used as name.

'''

from __future__ import (division as _py3_division,
                        print_function as _py3_print,
                        absolute_import as _py3_abs_import)


def suffix_kwd(name):
    '''Add an underscore suffix if name if a Python keyword.'''
    from xoutil.eight.values import iskeyword
    return '{}_'.format(name) if iskeyword(name) else name


def org_kwd(name):
    '''Remove the underscore suffix if name starts with a Python keyword.'''
    from xoutil.eight.values import iskeyword
    if name.endswith('_'):
        res = name[:-1]
        return res if iskeyword(res) else name
    else:
        return name


def getkwd(obj, name, default=None):
    '''Like `getattr` but taking into account Python keywords.'''
    return getattr(obj, suffix_kwd(name), default)


def setkwd(obj, name, value):
    '''Like `setattr` but taking into account Python keywords.'''
    setattr(obj, suffix_kwd(name), value)


def kwd_getter(obj):
    '''partial(getkwd, obj)'''
    from functools import partial
    return partial(getkwd, obj)


def kwd_setter(obj):
    '''partial(setkwd, obj)'''
    from functools import partial
    return partial(setkwd, obj)
