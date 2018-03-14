"""Record some usage of Numpy

"""
import numpy as np
import functools
import operator


def pick(from_array, pick_array):
    """Pick values specific in pick_array from param from_array.

    :param from_array: array to be pick
    :param pick_array: boolean array. Contain information of which value to be pick in from_array.
    :return:
    """
    from_array = np.array(from_array)
    pick_array = np.array(pick_array).astype(np.bool)
    return from_array[pick_array]


def operate(array, operate):
    """By default, can perform operate to every individual element of np array.

    >>> operate(np.array([1,2,3]), functools.partial(operator.mul, 2))

    :param array:
    :param operate:
    :return:
    """
    return operate(array)
