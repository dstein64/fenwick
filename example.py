from __future__ import print_function

from fenwick import FenwickTree

n = 10

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
print('* 2 through 8.                           ')
print('*******************************************')
print()

sum_2_8 = fenwick_tree.range_sum(2, 9)
print(sum_2_8)
print()

print('*******************************************')
print('* Calculate and print frequencies 5       ')
print('* through 9.                              ')
print('*******************************************')
print()

for x in range(5, 10):
    print(fenwick_tree[x])
print()

print('*******************************************')
print('* Retrieve and print all frequencies.      ')
print('*******************************************')
print()

print(fenwick_tree.frequencies())
