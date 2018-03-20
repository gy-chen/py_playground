"""Play pdb library

pdb document:
https://docs.python.org/3.6/library/pdb.html

test set_trace():
  $ python -m py_playground.pdb.__init__
  >>> test_set_trace()

"""
import random
import pdb


def test_set_trace():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    pdb.set_trace()
    print('a:', a, ', b:', b)
