Iteround: Sum-safe Rounding for Iterables
========================================

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



Feature Support
---------------

Iteround definitely supports at least these iterables.

- `list`
- `tuple`
- `dict`


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

.. _`the repository`: https://github.com/requests/requests
.. _AUTHORS: https://github.com/requests/requests/blob/master/AUTHORS.rst
