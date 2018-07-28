"""Record some usage of Numpy

TODO maybe I should just use Jupyter Notebook to record these.
"""
import functools
import operator
import scipy.cluster.vq
import numpy as np


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
    array([2, 4, 6])

    :param array:
    :param operate:
    :return:
    """
    return operate(array)


def vstack(arrays):
    """Suit for organize colors

    >>> a1 = np.array([20, 20, 20])
    >>> a2 = np.array([[234, 234, 234], [234, 234, 234]])
    >>> a3 = np.array([40, 40, 40])
    >>> np.vstack((a1, a2, a3))
    array([[ 20,  20,  20],
           [234, 234, 234],
           [234, 234, 234],
           [ 40,  40,  40]])

    :param arrays:
    :return:
    """
    return np.vstack(arrays)


def hstack(arrays):
    """Suit for organize colors

    >>> r = np.array([[20], [234], [234], [40]])
    >>> g = np.array([[20], [234], [234], [40]])
    >>> b = np.array([[20], [234], [234], [40]])
    >>> np.hstack((r, g, b))
    array([[ 20,  20,  20],
           [234, 234, 234],
           [234, 234, 234],
           [ 40,  40,  40]])

    :param arrays:
    :return:
    """
    return np.hstack(arrays)


def match_nearest_code(obs, code_book):
    """If want to match features to results of Kmeans or something like that.

    >>> obs = np.array([2, 8, 12, 18])
    >>> code_book = np.array([5, 10, 15])
    >>> scipy.cluster.vq.vq(obs, code_book)
    (array([0, 1, 1, 2]), array([ 3.,  2.,  2.,  3.]))

    :param obs:
    :param code_book:
    :return:
    """
    return scipy.cluster.vq.vq(obs, code_book)


def get_most_frequence_element(array):
    """Get most frequence appear element in the array

    >>> a1 = np.array([0, 1, 0, 1, 2, 0, 1, 0, 2])
    >>> unique, count = np.unique(a1, return_counts=True)
    >>> unique[count.argmax()]
    0

    :param array:
    :return:
    """
    unique, count = np.unique(array, return_counts=True)
    return unique[count.argmax()]


def axis_demo():
    """Demo what axis means

    >>> a1 = np.arange(1, 7).reshape((-1, 3))
    >>> np.sum(a1, axis=0, keepdims=True)
    array([[5, 7, 9]])
    >>> np.sum(a1, axis=1, keepdims=True)
    array([[ 6],
           [15]])

    :param array:
    :return:
    """
    a1 = np.arange(1, 7).reshape((-1, 3))
    assert False not in (np.sum(a1, axis=0, keepdims=True) == np.array([[5, 7, 9]]))
    assert False not in (np.sum(a1, axis=1, keepdims=True) == np.array([[6], [15]]))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
