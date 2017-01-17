#!/usr/bin/env python
"""Create a generator gen_seq() that creates the infinite geometric series:
1, 1/2, 1/4, 1/8...

Write a function first_N(num) that sums the first num values

Write a function until_small(epsilon) that sums the sequence until the
additional term is less than some small value epsilon.

Created on Sep 21, 2011

@author: paulross
"""

__author__  = 'Paul Ross'
__date__    = '2011-08-03'
__version__ = '0.1.0'
__rights__  = 'Copyright (c) 2011 Paul Ross. Copyright (c) 2015 AHL.'

import sys

import pytest

def gen_seq():
    x = 1.0
    while 1:
        yield x
        x *= 0.5


def first_N(num):

    sum = 0
    count = 0
    for i in gen_seq():
        if count >= num:
            break

        sum += i
        count += 1

    return sum


def until_small(epsilon):
    sum = 0
    for i in gen_seq():
        if i < epsilon:
            break

        sum += i
    return sum


def test_first_N():
    assert 0.0 == first_N(0)
    assert 1.0 == first_N(1)
    assert 1.5 == first_N(2)
    assert 1.75 == first_N(3)
    assert 1.875 == first_N(4)


def test_until_small():
    assert 1.5 == until_small(1.0 / 2)
    assert 1.875 == until_small(1.0 / 8)


def main():
    return pytest.main(__file__)


if __name__ == '__main__':
    sys.exit(main())

