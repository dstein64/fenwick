.. image:: https://github.com/dstein64/fenwick/workflows/build/badge.svg
    :target: https://github.com/dstein64/fenwick/actions

fenwick
=======

A Python library that implements Fenwick trees, based on the algorithm in
(Fenwick 1994).

Features
--------

- Update a frequency in ``O(log n)``.
- Retrieve a single frequency in ``O(log n)``.
- Initialize existing frequencies in ``O(n)``.
- Retrieve all frequencies in ``O(n)``.

Requirements
------------

*fenwick* supports ``python>=3.6``.

Linux, Mac, and Windows are supported.

Installation
------------

`fenwick <https://pypi.python.org/pypi/fenwick>`__ is available on PyPI, the Python Package Index.

::

    $ pip install fenwick

Documentation
-------------

See `documentation.md <https://github.com/dstein64/fenwick/blob/master/documentation.md>`__.

Example Usage
-------------

See `example.py <https://github.com/dstein64/fenwick/blob/master/example.py>`__.

Tests
-----

Tests are in `tests/ <https://github.com/dstein64/fenwick/blob/master/tests>`__.

::

    # Run tests
    $ python -m unittest discover tests -v

License
-------

The code in this repository has an `MIT License <https://en.wikipedia.org/wiki/MIT_License>`__.

See `LICENSE <https://github.com/dstein64/fenwick/blob/master/LICENSE>`__.

References
----------

Fenwick, Peter M. 1994. “A New Data Structure for Cumulative Frequency Tables.”
Software: Practice and Experience 24 (3): 327–36.
