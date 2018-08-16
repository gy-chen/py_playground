import numpy as np


def kfold(data, fold):
    """Split data using k fold method

    :param data: array
    :param fold: int
    :return: dict that contains {
        'train_1': np.array,
        'test_1': np.array,
        'train_2': np.array,
        'test_2': np.array,
        ...
        'train_k': np.array,
        'test_k': np.array
    }
    """
    data = np.array(data)
    fold_len = len(data) // fold
    result = {}
    for k in range(1, fold + 1):
        result['train{}'.format(k)] = np.concatenate([data[: fold_len * (k - 1)], data[fold_len * k:]])
        result['test{}'.format(k)] = data[fold_len * (k - 1): fold_len * k]
    return result
