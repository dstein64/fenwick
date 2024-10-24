import itertools
import unittest

from fenwick import FenwickTree


class TestFenwick(unittest.TestCase):
    def test_fenwick(self):
        n = 10
        frequencies = range(1, n + 1)
        cumsum = list(itertools.accumulate(frequencies))

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

        # Test find_stop()
        for value in range(-50, 101):
            stop = fenwick_tree_0.find_stop(value)
            self.assertNotEqual(stop, 0)
            if stop >= 1:
                self.assertGreaterEqual(fenwick_tree_0.prefix_sum(stop), value)
            if stop >= 2:
                self.assertLess(fenwick_tree_0.prefix_sum(stop - 1), value)
            if stop == -1:
                self.assertGreater(value, cumsum[-1])
            stop = fenwick_tree_0.find_stop(value, strict=True)
            self.assertNotEqual(stop, 0)
            if stop >= 1:
                self.assertGreater(fenwick_tree_0.prefix_sum(stop), value)
            if stop >= 2:
                self.assertLessEqual(fenwick_tree_0.prefix_sum(stop - 1), value)
            if stop == -1:
                self.assertGreaterEqual(value, cumsum[-1])
        self.assertEqual(FenwickTree(0).find_stop(10), -1)


if __name__ == '__main__':
    unittest.main()
