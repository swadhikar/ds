from collections import Counter

__all__ = ['mean', 'median', 'mode']


def mean(*args):
    try:
        total = sum(args)
        return total / len(args)
    except TypeError:
        print(f"ERROR: The mean(*args) function expects all it's "
              f"parameters to be of type 'int' or 'float'")
        raise


def _median(mid_index, *args):
    mid_but_before_num = args[mid_index - 1]
    mid_num = args[mid_index]
    return (mid_but_before_num + mid_num) / 2


def median(*args):
    size = len(args)
    mid_index = size // 2
    if size % 2 == 0:
        return _median(mid_index, *args)
    return args[mid_index]


def mode(*args):
    """Most frequent number"""
    counter = Counter(args)
    most_common_value, _ = counter.most_common()[0]
    return most_common_value


