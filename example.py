from __future__ import print_function

from fenwick import FenwickTree

n = 100

print('Note: Indexing is 0-based.')
print()

print('*******************************************')
print('* Initialize FenwickTree and update        ')
print('* frequencies one at a time.               ')
print('*******************************************')
print()

fenwick_tree = FenwickTree(n)
for x in range(n):
    fenwick_tree.add(x, x + 1)

print('*******************************************')
print('* Initialize FenwickTree using existing    ')
print('* frequencies.                             ')
print('*******************************************')
print()

fenwick_tree = FenwickTree(n)
f = range(1, n + 1)
fenwick_tree.init(f)

print('*******************************************')
print('* Calculate and print sum of all           ')
print('* frequencies                              ')
print('*******************************************')
print()

sum_all = fenwick_tree.prefix_sum(n)
print(sum_all)
print()

print('*******************************************')
print('* Calculate and print sum of frequencies   ')
print('* 10 through 20.                           ')
print('*******************************************')
print()

sum_10_20 = fenwick_tree.range_sum(10, 21)
print(sum_10_20)
print()

print('*******************************************')
print('* Calculate and print frequencies 30       ')
print('* through 35.                              ')
print('*******************************************')
print()

for x in range(30, 36):
    print(fenwick_tree[x])
