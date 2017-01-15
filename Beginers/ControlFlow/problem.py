"""
Write a program which returns 'Positive' 'Zero' or 'Negative' when given a number
"""


def what_sign(n):
    if n>0:
        return 'Positive'
    if n<0 :
        return 'Negative'

    return 'Zero'


def test_what_sign():
    assert what_sign(3) == 'Positive'
    assert what_sign(0) == 'Zero'
    assert what_sign(-3) == 'Negative'

"""
Write a program that prints the integers from 1 to 100.

But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz".
For numbers which are multiples of both three and five print "FizzBuzz".
"""

def fizzbuzz():

    for i in range(1, 100):
        fizz = 'Fizz' if i %3 else ''
        buzz = 'Buzz' if i%5 else ''

        to_print = i if (fizz =='' and buzz =='') else '%s%s' % (fizz, buzz)
        print to_print

"""
Write a function which removes one or more indicies from a list.

For example given the list:
["John", "Bob", "Charles", "Trev"]
and the indices:
[1, 2]
the resulting list will be:
["John", "Trev"]
"""

def remove_indices(mylist, idxs):
     for idx in idxs:
         mylist.remove(idx)

     return mylist

def test_remove_indices():
    assert remove_indices(["John", "Bob", "Charles", "Trev"], [0]) == ["Bob", "Charles", "Trev"]
    assert remove_indices(["John", "Bob", "Charles", "Trev"], [1, 2]) == ["John", "Trev"]


""""
Modify connect to handle failed connections
"""
import random


def open_connection():
    if random.randint(0, 3) != 0:
        raise ValueError('failed to connect')
    return True


def connect(nretry=100):
    for _ in xrange(nretry):
        try:
         if open_connection():
            return
        except ValueError:
            print 'Trying connection %i over %i retries' % (_, nretry)

connect()
