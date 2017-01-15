#!/usr/bin/env python
"""Write an equivalent function to the build in filter() function that takes
a function and a single list and returns a new list of elements where the
function evaluates to true.
Call your function _filter().

For example: _filter(lambda x: x > 0, [1,-2, 3,-4])
(the lambda returns True if x is positive) returns:
[1, 3]

Write an equivalent function to the build in map() function that takes
a function and a single sequence and returns a new list of elements where the
function has been applied to each element of the sequence.
Call your function _map().

For example: _map(lambda x: x.upper(), 'abcdef')
returns:
['A', 'B', 'C', 'D', 'E', 'F']

NOTE: You might want to study the Python documentation for what is meant to
happen when the function is None.


Created on Sep 6, 2011

@author: paulross
"""

__author__  = 'Paul Ross'
__date__    = '2011-08-03'
__version__ = '0.1.0'
__rights__ = 'Copyright (c) 2011 Paul Ross. Copyright (c) 2015 AHL.'

import sys

import pytest


def _filter(fn, iterable):
    return [item for item in iterable if (fn is [None] and item) or fn(item)]


def _map(fn, iterable):
    return [item if fn is [None] else fn(item) for item in iterable]


def test_filter():
    seq = [1, -2, 3, -4]
    assert(filter(lambda x: x > 0, seq) == _filter(lambda x: x > 0, seq))


def test_map():
    seq = 'abcdef'
    assert(map(lambda x: x.upper(), seq) == _map(lambda x: x.upper(), seq))


def main():
    return pytest.main(__file__)

if __name__ == '__main__':
    sys.exit(main())
