import unittest
import itertools
import bisect

from fenwick import FenwickTree


class TestFenwick(unittest.TestCase):
    def test_fenwick(self):
        n = 10
        frequencies = range(1, n + 1)

        # Test a Fenwick tree initialized with existing frequencies
        fenwick_tree_0 = FenwickTree(n)
        fenwick_tree_0.init(frequencies)
        self.assertEqual(fenwick_tree_0.frequencies(), list(frequencies))
        for idx in range(len(frequencies)):
            self.assertEqual(fenwick_tree_0.prefix_sum(idx + 1), sum(frequencies[:idx + 1]))
        for i in range(len(frequencies)):
            for j in range(i + 1, len(frequencies) + 1):
                self.assertEqual(fenwick_tree_0.range_sum(i, j), sum(frequencies[i:j]))
        for idx in range(len(frequencies)):
            self.assertEqual(fenwick_tree_0[idx], frequencies[idx])

        # Test a Fenwick tree initialized one frequency at a time
        fenwick_tree_1 = FenwickTree(n)
        for idx, x in enumerate(frequencies):
            fenwick_tree_1.add(idx, x)
        self.assertEqual(fenwick_tree_1.frequencies(), list(frequencies))
        for idx in range(len(frequencies)):
            self.assertEqual(fenwick_tree_1.prefix_sum(idx + 1), sum(frequencies[:idx + 1]))
        for i in range(len(frequencies)):
            for j in range(i + 1, len(frequencies) + 1):
                self.assertEqual(fenwick_tree_1.range_sum(i, j), sum(frequencies[i:j]))
        for idx in range(len(frequencies)):
            self.assertEqual(fenwick_tree_1[idx], frequencies[idx])

        self.assertEqual(fenwick_tree_0, fenwick_tree_1)
        
        
    def test_bisect_left(self):
        
        # Create a Fenwick tree
        frequencies = [1, 2, 3]
        n = len(frequencies)
        tree = FenwickTree(n)
        tree.init(frequencies)
        
        # Create a cumulative sum
        cumsum = list(itertools.accumulate(frequencies))
        test_values = [-5, 0.5, 1, 2, 3, 7]
        
        for test_value in test_values:
            # Indexing the FenwickTree
            index_fenwick = tree.bisect_right(test_value)
            index_bisect = bisect.bisect_right(cumsum, test_value)
            self.assertEqual(index_fenwick, index_bisect)
            
            
        # Test a specific edge case. The cumsums are [1, 3, 6], and the 
        # smallest index i such that cumsum[i] > 3 is 2.
        self.assertEqual(tree.bisect_right(3), 2)


if __name__ == '__main__':
    unittest.main()
