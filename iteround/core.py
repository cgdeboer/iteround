from __future__ import absolute_import, division, print_function
from collections import OrderedDict

SMALLEST = 'smallest'
LARGEST = 'largest'
DIFFERENCE = 'difference'


def saferound(iterable, places, strategy=DIFFERENCE, rounder=round, topline=None):
    """Rounds an iterable of floats while retaining the original summed value.

    Function parameters should be documented in the ``Args`` section. The name
    of each parameter is required. The type and description of each parameter
    is optional, but should be included if not obvious.

    Args:
        iterable (list, dict, set, numpy.array, generator): list(y) of numbers
            If a dict is passed in, the values must be all floats.

        places (int): Places for rounding.
            Number of places each item in the set should be rounded to.

        strategy (str, optional): The strategy used to clean up rounding errors
            'difference', 'largest', 'smallest'. Defaults to 'difference'

            'difference' seeks to minimize the sum of the array of the
            differences between the original value and the rounded value of
            each item in the iterable. It will adjust the items with the
            largest difference to preserve the sum. This is the default.

            'largest' for any post rounding adjustments, sort the array by
            the largest values to smallest and adjust those first.

            'smallest' for any post rounding adjustments, sort the array by
            the smallest values to largest, adjust the smaller ones first.

        rounder (method, optional): The rounding function. Defaults to `round`

            rounder method must take 2 arguments, a `float` to be rounded, and
            an integer for the number of places (with support for negative)

        topline (float, optional): Topline to match
            Useful in places where we want the total sum to match a different
            topline than the sum of iterable. This can useful in cases where
            original values are altered before passing into the saferound
            method, but the original sum needs to be maintained.

    Returns:
        iterable (same type as input, but with rounded values).

            if 'dict' or 'tuple' are passed, result will be dict or tuple.
            All other iterables (range, map, np.array, etc) will return
            list.

    Raises:
        AssertionError
            - places is not an integer
            - strategy is not valid
            - values are not all floats
    """
    assert isinstance(places, int)
    assert strategy in [SMALLEST, LARGEST, DIFFERENCE]
    values = iterable
    if (isinstance(iterable, dict) or isinstance(iterable, OrderedDict)):
        keys, values = zip(*iterable.items())
    assert all([isinstance(x, float) for x in values])

    # define a sorting method for rounded differences
    sorter = _sort_by_diff if strategy == DIFFERENCE else _sort_by_value
    default_reverse = False if strategy == SMALLEST else True

    # calculate original sum, rounded,  then rounded local sum.
    local = [Number(i, value) for i, value in enumerate(values)]
    orig_sum = (_sumnum(local, places, rounder)
                if topline is None else
                rounder(topline, places))
    [n.round(places, rounder) for n in local]
    local_sum = _sumnum(local, places, rounder)

    # adjust values to adhere to original sum
    while local and local_sum != orig_sum:
        diff = rounder(orig_sum - local_sum, places)
        if diff < 0.:
            increment = -1 * _mininc(places)
            reverse = False if strategy == DIFFERENCE else default_reverse
        else:
            increment = _mininc(places)
            reverse = True if strategy == DIFFERENCE else default_reverse
        tweaks = int(abs(diff) / _mininc(places))
        local = sorter(local, reverse)
        for ith in range(0, min(tweaks, len(local))):
            local[ith].value += increment
            local[ith].round(places, rounder)
        local_sum = _sumnum(local, places, rounder)

    # return a proper type if passed, else return list
    rounded_list = [n.value for n in _sort_by_order(local)]
    if isinstance(iterable, dict):
        return dict(zip(keys, rounded_list))
    elif isinstance(iterable, OrderedDict):
        return OrderedDict(zip(keys, rounded_list))
    elif isinstance(iterable, tuple):
        return tuple(rounded_list)
    return rounded_list


def _sumnum(numbers, places, rounder):
    return rounder(sum([n.value for n in numbers]), places)


def _sort_by_value(numbers, reverse):
    return sorted(numbers, key=lambda x: x.value, reverse=reverse)


def _sort_by_order(numbers):
    return sorted(numbers, key=lambda x: x.order)


def _sort_by_diff(numbers, reverse):
    return sorted(numbers, key=lambda x: x.diff, reverse=reverse)


def _mininc(places):
    return 1 / (10**places)


class Number(object):
    def __init__(self, order, value):
        self.value = float(value)
        self.order = order
        self.original = float(value)
        self.diff = None

    def round(self, places, rounder):
        self.value = rounder(self.value, places)
        self.diff = self.original - self.value

    def __repr__(self):
        return '{} <- {} ({})'.format(self.value, self.original, self.diff)
