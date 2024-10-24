Documentation
-------------

To use *fenwick*, first import the *fenwick* module.

    >>> import fenwick
    
### Example Usage

See [example.py](example.py)

### Initialization

The data structure is initialized with *fenwick.FenwickTree*.
    
    >>> from fenwick import FenwickTree
    >>> fenwick_tree = FenwickTree(5)

*fenwick.FenwickTree* takes the following arguments:

* **n** The number of items.

The *init* method initializes the Fenwick tree with existing frequencies,
in O(n).

    >>> fenwick_tree.init([10, 4, 0, 2, 16])

*fenwick.FenwickTree.init* takes the following arguments:

* **frequencies** A sequence with existing frequencies.

### Updating Frequencies

Indexing is 0-based.

The *add* method updates an element's frequency, in O(log n).

    >>> fenwick_tree.add(3, 7) # Adds 7 to element 3's frequency

*fenwick.FenwickTree.add* takes the following arguments:

* **idx** The index of the element to update.
* **k** The update increment.

### Retrieving Frequencies

Indexing is 0-based.

The *prefix_sum* method calculates the cumulative sum of the initial elements
in O(log n).

    >>> fenwick_tree.prefix_sum(5)

*fenwick.FenwickTree.prefix_sum* takes the following arguments:

* **stop** The stop index (exclusive).

The *range_sum* method calculates the cumulative sum of a range of elements
in O(log n).

    >>> fenwick_tree.range_sum(5, 10)

*fenwick.FenwickTree.range_sum* takes the following arguments:

* **start** The start index (inclusive).
* **stop** The stop index (exclusive).

An individual frequency can be accessed in O(log n).

    >>> freq_10 = fenwick_tree[10]

The *frequencies* method retrieves a list of all frequencies in O(n). This
is more efficient than retrieving each individual frequency separately, which
would be O(n log n).

    >>> freqs = fenwick_tree.frequencies()

### Stop Search

For a specified value, the *find_stop* method returns the smallest stop for
which `prefix_sum(stop) >= value`, or -1 if there is no stop that would satisfy
the condition. The time complexity is O(log n).

    >>> stop = fenwick_tree.find_stop(20)

*fenwick.FenwickTree.find_stop* takes the following arguments:

* **value** The threshold.
* **strict** (optional) When True, the condition changes to `prefix_sum(stop) > value`.
