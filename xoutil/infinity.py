#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# ---------------------------------------------------------------------
# infinity
# ---------------------------------------------------------------------
# Copyright (c) 2016, 2017 Merchise Autrement and Contributors
# All rights reserved.
#
# This is free software; you can redistribute it and/or modify it under the
# terms of the LICENCE attached (see LICENCE file) in the distribution
# package.
#
# Created on 2016-07-04

'''The Infinity value.

Not all values are comparable with Infinity by default.  The ABC
`InfinityComparable`:class: holds the registry of such values.  Any `number
<numbers.Number>`:class: is comparable with `Infinity`:obj:.

`Dates <datetime.date>`:class:, `datetimes <datetime.datetime>`:class: and
`time deltas <datetime.timedelta>`:class: are also supported.

.. warning:: In Python 2, dates, datetimes and time deltas must be the right
             operand, as in ``Infinity > today``.  Doing ``today < Infinity``
             fails in Python 2.

'''

from __future__ import (division as _py3_division,
                        print_function as _py3_print,
                        absolute_import as _py3_abs_import)


import abc
import datetime
from numbers import Number
from functools import total_ordering

from xoutil.eight.meta import metaclass


class InfinityComparable(metaclass(abc.ABCMeta)):
    '''Any type that can be sensibly compared to infinity.

    By default, all types in the number tower are comparable; and
    `datetime.date`:class:, `datetime.datetime`:class:, and
    `datetime.timedelta`:class:.

    '''

    @classmethod
    def __subclasshook__(self, cls):
        if isinstance(cls, type) and issubclass(cls, Number):
            return True
        else:
            return NotImplemented


InfinityComparable.register(datetime.date)
InfinityComparable.register(datetime.datetime)
InfinityComparable.register(datetime.timedelta)


@total_ordering
class InfinityType(object):
    _positive = None
    _negative = None

    def __new__(cls, sign):
        if sign < 0:
            res = cls._negative
            if not res:
                cls._negative = res = object.__new__(cls)
        else:
            res = cls._positive
            if not res:
                cls._positive = res = object.__new__(cls)
        return res

    def __init__(self, sign):
        self.sign = -1 if sign < 0 else 1

    def __lt__(self, other):
        if isinstance(other, InfinityComparable):
            return self.sign < 0   # True iff -Infinity
        elif isinstance(other, InfinityType):
            return self.sign < other.sign
        else:
            raise TypeError(
                'Incomparable types: %r and %r' % (type(self), type(other))
            )

    def __eq__(self, other):
        if isinstance(other, InfinityType):
            return self.sign == other.sign
        else:
            return False

    def __neg__(self):
        return type(self)(-self.sign)

    def __str__(self):
        return '∞' if self.sign > 0 else '-∞'

    def __repr__(self):
        return 'Infinity' if self.sign > 0 else '-Infinity'


Infinity = InfinityType(+1)
