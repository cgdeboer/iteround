Iteround: Sum-safe Rounding for Iterables
========================================
.. image:: https://travis-ci.org/cgdeboer/iteround.svg?branch=master
    :target: https://travis-ci.org/cgdeboer/iteround

.. image:: https://img.shields.io/pypi/v/iteround.svg
    :target: https://pypi.org/project/iteround/

Iteround is an organic (standard library) sum-safe rounding library for Python
iterables (lists, tuples, dicts).

.. image:: https://raw.githubusercontent.com/cgdeboer/iteround/master/docs/iteround.png


Example Code:

.. code-block:: python

    >>> import iteround
    >>> data = {'foo': 60.19012964572332,
                'bar': 15.428802458406679,
                'baz': 24.381067895870007}
    >>> sum(data.values())
    100.0
    >>> rounded = iteround.saferound(data, 0)
    >>> rounded
    {'foo': 60.0,
     'bar': 16.0,
     'baz': 24.0}
    >>> sum(rounded.values())
    100.0

How It Works
---------------
Iteround provides a single method, called :code:`saferound` that takes the
following inputs:

iterable (list, dict, set, numpy.array, generator): list(y) of numbers
    If a dict is passed in, the values must be all floats.

places (int): Places for rounding.
    Number of places each item in the set should be rounded to.
	
topline (float, optional): Topline to match
	Useful in places where we want the total sum to match a different topline 
	than the sum of iterable. This can useful in cases where original values 
	are altered before passing into the saferound method, but the original sum
	needs to be maintained.

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

    Strategy strings are available as:
        :code:`iteround.DIFFERENCE`
        :code:`iteround.LARGEST`
        :code:`iteround.SMALLEST`

If 'dict' or 'tuple' are passed, result will be dict or tuple.
All other iterables (range, map, np.array, etc) will return
list.



Feature Support
---------------

Iteround definitely supports at least these iterables.

- `list`
- `tuple`
- `dict`
- `OrderedDict`


Iteround officially supports Python 2.7 & 3.4–3.6.

Installation
------------

To install Iteround, use `pipenv <http://pipenv.org/>`_ (or pip, of course):

.. code-block:: bash

    $ pipenv install iteround

Documentation
-------------

Documentation beyond this readme will be available soon.


How to Contribute
-----------------

#. Check for open issues or open a fresh issue to start a discussion around a feature idea or a bug.
#. Fork `the repository`_ on GitHub to start making your changes to the **master** branch (or branch off of it).
#. Write a test which shows that the bug was fixed or that the feature works as expected.
#. Send a pull request. Make sure to add yourself to AUTHORS_.

.. _`the repository`: https://github.com/cgdeboer/iteround
.. _AUTHORS: https://github.com/cgdeboer/iteround/blob/master/AUTHORS.rst
