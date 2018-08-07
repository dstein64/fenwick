from __future__ import print_function

import os
import sys

version_txt = os.path.join(os.path.dirname(__file__), 'version.txt')
with open(version_txt, 'r') as f:
    __version__ = f.read().strip()

# ************************************************************
# * Utils
# ************************************************************

_major_version = sys.version_info.major
if _major_version not in (2, 3):
    raise RuntimeError("Unsupported version of Python: {}".format(_major_version))


def _range(*args, **kwargs):
    if _major_version == 2:
        import __builtin__
        return __builtin__.xrange(*args, **kwargs)
    else:
        import builtins
        return builtins.range(*args, **kwargs)

# ************************************************************
# * Core
# ************************************************************

class FenwickTree(object):
    """
    A data structure for maintaining cumulative (prefix) sums.
    (aka "binary indexed tree")
    Incrementing a value is O(log n).
    Calculating a cumulative sum is O(log n).
    Retrieving a single frequency is a special case of calculating a cumulative
    sum, and is thus O(log n).
    """
    def __init__(self, n):
        """ Initializes n frequencies to zero. """
        self._n = n
        self._v = [0] * n

    def __len__(self):
        return self._n

    def prefix_sum(self, stop):
        """ Returns sum of first elements (sum upto *stop*, exclusive). """
        if stop <= 0 or stop > self._n:
            raise IndexError()
        _sum = 0
        while stop > 0:
            _sum += self._v[stop - 1]
            stop &= stop - 1
        return _sum

    def range_sum(self, start, stop):
        """ Returns sum from start (inclusive) to stop (exclusive). """
        if start < 0 or start >= self._n:
            raise IndexError()
        if stop <= start or stop > self._n:
            raise IndexError()
        result = self.prefix_sum(stop)
        if start > 0:
            result -= self.prefix_sum(start)
        return result

    def __getitem__(self, idx):
        return self.range_sum(idx, idx + 1)

    def add(self, idx, k):
        """ Adds k to idx'th element (0-based indexing). """
        if idx < 0 or idx >= self._n:
            raise IndexError()
        idx += 1
        while idx <= self._n:
            self._v[idx - 1] += k
            idx += idx & -idx

    def init(self, frequencies):
        """ Initialize in O(n) with specified frequencies. """
        if len(frequencies) != self._n:
            raise ValueError()
        for idx in _range(self._n):
            self._v[idx] = frequencies[idx]
        for idx in _range(1, self._n + 1):
            parent_idx = idx + (idx & -idx) # parent in update tree
            if parent_idx <= self._n:
                self._v[parent_idx - 1] += self._v[idx - 1]
