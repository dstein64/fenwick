import operator
import os
import sys

version_txt = os.path.join(os.path.dirname(__file__), 'version.txt')
with open(version_txt, 'r') as f:
    __version__ = f.read().strip()

# ************************************************************
# * Utils
# ************************************************************

_major_version = sys.version_info.major
if _major_version < 3:
    raise RuntimeError("Unsupported version of Python: {}".format(_major_version))

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
        """Initializes n frequencies to zero."""
        self._n = n
        self._v = [0] * n

    def __len__(self):
        return self._n

    def prefix_sum(self, stop):
        """Returns sum of first elements (sum up to *stop*, exclusive)."""
        if stop <= 0 or stop > self._n:
            raise IndexError()
        _sum = 0
        while stop > 0:
            _sum += self._v[stop - 1]
            stop &= stop - 1
        return _sum

    def find_stop(self, value, strict=False):
        """
        Returns the smallest stop for which prefix_sum(stop) >= value, or -1 if
        there is no stop that would satisfy the condition. When strict is True,
        the condition changes to prefix_sum(stop) > value.
        """
        # Algorithm from https://stackoverflow.com/a/34701217/1509433
        base = -1
        # round len(self) down to a power of 2 if len(self) > 0, else round up
        step = 1 << max(len(self).bit_length() - 1, 0)
        compare = operator.ge if strict else operator.gt
        while step > 0:
            idx = base + step
            if idx < len(self) and compare(value, self._v[idx]):
                value -= self._v[idx]
                base = idx
            step >>= 1
        return base + 2 if 0 < base + 2 <= len(self) else -1

    def range_sum(self, start, stop):
        """Returns sum from start (inclusive) to stop (exclusive)."""
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

    def frequencies(self):
        """Retrieves all frequencies in O(n)."""
        _frequencies = [0] * self._n
        for idx in range(1, self._n + 1):
            _frequencies[idx - 1] += self._v[idx - 1]
            parent_idx = idx + (idx & -idx)
            if parent_idx <= self._n:
                _frequencies[parent_idx - 1] -= self._v[idx - 1]
        return _frequencies

    def add(self, idx, k):
        """Adds k to idx'th element (0-based indexing)."""
        if idx < 0 or idx >= self._n:
            raise IndexError()
        idx += 1
        while idx <= self._n:
            self._v[idx - 1] += k
            idx += idx & -idx

    def __setitem__(self, idx, value):
        # It's more efficient to use add directly, as opposed to
        # __setitem__, since the latter calls __getitem__.
        self.add(idx, value - self[idx])

    def init(self, frequencies):
        """Initialize in O(n) with specified frequencies."""
        n = len(frequencies)
        if n != self._n:
            raise ValueError(f'length of frequencies ({n}) does not match length of FenwickTree ({self._n})')
        self._v[:] = frequencies
        for idx in range(1, self._n + 1):
            parent_idx = idx + (idx & -idx)  # parent in update tree
            if parent_idx <= self._n:
                self._v[parent_idx - 1] += self._v[idx - 1]

    def __eq__(self, other):
        return isinstance(other, FenwickTree) and self._n == other._n and self._v == other._v
